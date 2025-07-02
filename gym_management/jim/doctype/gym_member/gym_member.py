# Copyright (c) 2025, Jayz and contributors
# For license information, please see license.txt

# import frappe
# gym_management/gym_management/doctype/gym_member/gym_member.py

from frappe.model.document import Document
import frappe

from frappe.model.document import Document
import frappe

class GymMember(Document):

    def validate(self):
        self.update_active_membership()

    def update_active_membership(self):
        # Find the latest active membership for this member
        if self.name:
            active_membership = frappe.get_all(
                "Gym Membership",
                filters={
                    "member": self.name,
                    "status": "Active"
                },
                order_by="start_date desc",
                limit_page_length=1
            )
            if active_membership:
                self.active_membership = active_membership[0].name
            else:
                self.active_membership = None
