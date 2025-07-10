import frappe

def execute(filters=None):
    # Step 1: Get the logged-in user
    user = frappe.session.user

    # Step 2: Get the email ID from Gym Membership (assuming 'email_id' field maps to frappe user)
    email = frappe.get_value("Gym Membership", {"email_id": user}, "email_id")

    if not email:
        frappe.throw("No Gym Membership found for the current user.")

    # Step 3: Fetch metrics from the child table of BMI
    data = frappe.db.sql("""
        SELECT
            m.date,
            m.current_weight,
            m.current_height,
            m.daily_calorie_intake,
            m.bmi
        FROM
            `tabBMI` b
        JOIN
            `tabMetrics Update` m ON m.parent = b.name
        WHERE
            b.email = %s
        ORDER BY
            m.date ASC
    """, (email,), as_dict=True)

    # Step 4: Define columns
    columns = [
        {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 120},
        {"label": "Weight (kg)", "fieldname": "current_weight", "fieldtype": "Float", "width": 120},
        {"label": "Height (cm)", "fieldname": "current_height", "fieldtype": "Float", "width": 120},
        {"label": "Daily Calories", "fieldname": "daily_calorie_intake", "fieldtype": "Int", "width": 140},
        {"label": "BMI", "fieldname": "bmi", "fieldtype": "Float", "width": 100},
    ]

    return columns, data
