# import frappe

# def redirect_after_login(login_manager):
#     user = frappe.session.user
#     roles = frappe.get_roles(user)

#     # Set custom redirect location
#     if "Gym Member" in roles:
#         frappe.local.response["type"] = "redirect"
#         frappe.local.response["location"] = "/my-gym-profile"

#     elif "Gym Trainer" in roles:
#         frappe.local.response["type"] = "redirect"
#         frappe.local.response["location"] = "/trainer-dashboard"

#     else:
#         frappe.local.response["type"] = "redirect"
#         frappe.local.response["location"] = "/app"
