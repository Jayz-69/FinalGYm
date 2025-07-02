# apps/gym_management/gym_management/jim/api.py

# apps/gym_management/gym_management/jim/api.py

import frappe

@frappe.whitelist()
def update_total_lockers(lockers_used):
    """Reduces the total lockers in Gym Settings by lockers_used amount"""
    lockers_used = int(lockers_used)

    settings = frappe.get_single("Gym Settings")
    total_lockers = settings.total_lockers or 0

    if lockers_used > total_lockers:
        return {
            "success": False,
            "message": "Not enough lockers available"
        }

    settings.total_lockers = total_lockers - lockers_used
    settings.save()

    return {
        "success": True,
        "remaining": settings.total_lockers
    }

