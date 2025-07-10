# gym_management/gym_management/jim/api.py

import frappe
import json
from datetime import datetime

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



import frappe
from frappe.auth import LoginManager
from frappe import _

@frappe.whitelist()
def authenticate_user(email, password, role):
    """Authenticate the user using email, password, and role."""

    # Step 1: Check if the email exists in the Gym Members table
    gym_member = frappe.get_all(
        "Gym Member", 
        filters={"email": email}, 
        fields=["name1", "role", "password"]  # Include plain-text password field
    )

    if not gym_member:
        return {"success": False, "message": "Invalid email"}  # Return 'Invalid email' if not found

    # Step 2: Retrieve the plain-text password stored in the database
    stored_password = gym_member[0]["password"]
    
    # Step 3: Compare the plain-text password with the one stored in the database
    if stored_password != password:
        return {"success": False, "message": "Invalid password"}  # Return 'Invalid password' if not matched
    
    # Step 4: Check if the provided role matches the one in the database
    if gym_member[0]["role"] != role:
        return {"success": False, "message": "Invalid role"}  # Return 'Invalid role' if not matched

    # Return success message with role
    return {"success": True, "message": "Authentication successful", "role": gym_member[0]["role"]}




from datetime import datetime
import frappe

# @frappe.whitelist(allow_guest=True)
# def get_member_summary(email):
#     # Step 1: Get Gym Membership Doc
#     membership = frappe.get_doc("Gym Membership", email)

#     # Step 2: Calculate remaining days
#     today = datetime.today().date()
#     end_date = membership.end_date
#     remaining_days = (end_date - today).days if end_date else None

#     # Step 3: Get trainer name from Gym Class Booking
#     trainer_name = ""
#     booking = frappe.get_all(
#         "Gym Class Booking",
#         filters={"gym_member": email},
#         fields=["trainer_name"],
#         limit=1
#     )

#     if booking and booking[0].trainer_name:
#         try:
#             trainer_doc = frappe.get_doc("TrainerReg", booking[0].trainer_name)
#             trainer_name = trainer_doc.name1
#         except:
#             trainer_name = "Trainer not found"

#     # Step 4: Return required fields
#     return {
#         "member_name": membership.name1,
#         "joining_date": membership.start_date,
#         "ending_date": membership.end_date,
#         "plan_type": membership.plan_type,
#         "remaining_days": remaining_days,
#         "trainer_name": trainer_name
#     }
@frappe.whitelist(allow_guest=True)
def get_member_details(email):
# Fetch membership info

    membership = frappe.get_doc("Gym Membership", email)

    # Calculate remaining days
    today = datetime.today().date()
    ending_date = membership.end_date
    remaining_days = (ending_date - today).days if ending_date else None

    # Get assigned trainer from Gym Class Booking
    booking = frappe.get_all("Gym Class Booking",
    filters={"email": email},
    fields=["trainer_name"],
    limit_page_length=1)

    trainer_name = booking[0].trainer_name if booking else None
    trainer_info = {}

    if trainer_name:
        trainer = frappe.get_doc("TrainerReg", trainer_name)
        trainer_info = {
        "name": trainer.name,
        "email_id": trainer.email_id,
        "contact_no": trainer.contact_no,
        "address": trainer.address,
        "gender": trainer.gender
        }

    return {
    "email": membership.email_id,
    "contact": membership.contact_number,
    "plan": membership.plan_type,
    "joining_date": membership.start_date,
    "ending_date": membership.end_date,
    "remaining_days": remaining_days,
    "trainer": trainer_info
    }
