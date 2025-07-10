# Copyright (c) 2025, Jayz and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document


class GymMember(Document):
    # def after_insert(self):
    #     self.create_user()

    # def create_user(self):
    #     if not self.email:
    #         frappe.throw("Email is required to create user.")

    #     if frappe.db.exists("User", self.email):
    #         frappe.msgprint(f"User {self.email} already exists.")
    #         return

    #     # Create the user
    #     user = frappe.get_doc({
    #         "doctype": "User",
    #         "email": self.email,
    #         "first_name": self.full_name,
    #         "send_welcome_email": 1,
    #         "user_type": "Website User"
    #     })

    #     # Assign role from the select field
    #     if self.role:
    #         user.append("roles", {"role": self.role})

    #     user.insert(ignore_permissions=True)
    #     frappe.msgprint(f"User {self.email} created and role {self.role} assigned.")

    pass