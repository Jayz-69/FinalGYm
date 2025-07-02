import frappe
from frappe.model.document import Document
from datetime import datetime, timedelta

class GymMembership(Document):

    def validate(self):
        self.calculate_final_price()
        self.calculate_end_date()
        self.set_locker_description()

    def on_submit(self):
        self.update_lockers(allocate=True)

    def on_cancel(self):
        self.safe_update_lockers(False)

    def on_trash(self):
        self.safe_update_lockers(False)

    def safe_update_lockers(self, allocate):
        try:
            self.update_lockers(allocate)
        except Exception as e:
            frappe.log_error(e, f"Locker update failed for {self.name}")

    def update_lockers(self, allocate=True):
        settings = frappe.get_single("Gym Settings")
        locker_count = int(self.locker or 0)
        old_used = settings.used_lockers or 0

        if allocate:
            new_used = old_used + locker_count
            if new_used > settings.total_lockers:
                frappe.throw(f"Not enough lockers available. Available: {settings.total_lockers - old_used}")
        else:
            new_used = max(0, old_used - locker_count)

        # Directly update DB ignoring read-only flags
        frappe.db.set_value("Gym Settings", settings.name, "used_lockers", new_used)
        frappe.db.commit()
        frappe.log_error(f"Updated used_lockers to {new_used}", "Locker Count Updated")

    def calculate_final_price(self):
        settings = frappe.get_single("Gym Settings")
        mapping = {
            "1 Month": settings.default_price_1m,
            "3 Months": settings.default_price_3m,
            "1 Year": settings.default_price_1y,
        }
        plan_key = (self.plan_type or "").split(">>")[0].strip()
        base_price = mapping.get(plan_key, 0)
        locker_price = int(self.locker or 0) * settings.locker_price_1m
        self.final_price = base_price + locker_price

    def calculate_end_date(self):
        if self.start_date and self.plan_type:
            if isinstance(self.start_date, str):
                self.start_date = datetime.strptime(self.start_date, "%Y-%m-%d").date()
            days = {"1 Month":30, "3 Months":90, "1 Year":365}.get(self.plan_type.split(">>")[0].strip(), 0)
            self.end_date = self.start_date + timedelta(days=days) if days else None
        else:
            self.end_date = None

    def set_locker_description(self):
        count = int(self.locker or 0)
        if count > 0:
            import random
            locks = [f"L{random.randint(100,999)}" for _ in range(count)]
            self.locker_description = "Assigned Lockers: " + ", ".join(locks)
        else:
            self.locker_description = ""
