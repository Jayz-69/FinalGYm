# apps/gym_management/gym_management/jim/api.py

import frappe

@frappe.whitelist()
def get_locked_member_count():
    return frappe.db.count("Gym Member", {"locker": "Yes"})
