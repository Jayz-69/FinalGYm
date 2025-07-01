# Copyright (c) 2025, Jayz and contributors
# For license information, please see license.txt

# import frappe
# gym_membership.py
# Copyright (c) 2025, Jayz and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import frappe

class GymMembership(Document):

    def validate(self):
        self.calculate_final_price()

    def calculate_final_price(self):
        settings = frappe.get_single("Gym Settings")
        plan_price_map = {
            "1 Month": settings.default_price_1m,
            "3 Months": settings.default_price_3m,
            "1 Year": settings.default_price_1y,
        }

        # Extract plan duration from plan_type string if it contains extra text
        plan_duration = self.plan_type.split(">>")[0].strip() if ">>" in self.plan_type else self.plan_type

        plan_price = plan_price_map.get(plan_duration, 0)
        locker_price = settings.locker_price_1m if self.locker == "Yes" else 0
        self.final_price = plan_price + locker_price

    def on_submit(self):
        # Update the active_membership field in Gym Member
        if self.status == "Active" and self.member:
            frappe.db.set_value("Gym Member", self.member, "active_membership", self.name)
            frappe.db.commit()

    def on_cancel(self):
        if self.member:
            frappe.db.set_value("Gym Member", self.member, "active_membership", None)
            frappe.db.commit()
