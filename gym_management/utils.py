import frappe

def redirect_after_login(login_manager):
    user = frappe.session.user
    roles = frappe.get_roles(user)

    # Clear previous last_visited page so it doesn't take over
    frappe.local.response.pop("home_page", None)

    # Role-based redirection
    if "Gym Admin" in roles:
        frappe.local.response["home_page"] = "/admin-dashboard"

    elif "Gym Member" in roles:
        # ✅ Redirect to the portal Web Form page using email as name
        frappe.local.response["home_page"] = f"/gym-subscription/{user}"

    elif "Gym Trainer" in roles:
        frappe.local.response["home_page"] = "/trainer-profile"

    else:
        frappe.local.response["home_page"] = f"/gym-subscription/{user}"
