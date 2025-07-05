# gym_management/gym_management/jim/api.py

import frappe
import json

@frappe.whitelist()
def update_total_lockers(lockers_used):
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

@frappe.whitelist()
def get_filtered_trainers(doctype, txt, searchfield, start, page_len, filters=None):
    if filters and isinstance(filters, str):
        filters = json.loads(filters)
    elif not filters:
        filters = {}

    specialization = filters.get("specialization")
    conditions = []
    values = []

    if specialization:
        conditions.append("trainer_specialization = %s")
        values.append(specialization)

    start = int(start)
    page_len = int(page_len)

    query = f"""
        SELECT name, full_name FROM `tabGym Trainer`
        WHERE {searchfield} LIKE %s
    """

    values = [f"%{txt}%"] + values

    if conditions:
        query += " AND " + " AND ".join(conditions)

    query += " LIMIT %s OFFSET %s"
    values += [page_len, start]

    results = frappe.db.sql(query, values, as_dict=True)

    # Format dropdown options
    return [{"value": r["name"], "label": r["full_name"]} for r in results]