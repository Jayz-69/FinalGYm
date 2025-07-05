import frappe

def execute(filters=None):
    if not filters or not filters.get("member"):
        frappe.throw("Please select a Member")

    member = filters.get("member")

    # 1) Fetch data
    data = frappe.db.sql("""
        SELECT
            mu.date as date,
            mu.current_weight,
            mu.daily_calorie_intake,
            mu.bmi
        FROM `tabMetrics Update` mu
        JOIN `tabGym Membership` gm ON mu.parent = gm.name
        WHERE gm.member = %s
        ORDER BY mu.date ASC
    """, (member,), as_dict=True)

    # 2) Columns
    columns = [
        {"label": "Date",            "fieldname": "date",                  "fieldtype": "Date",  "width": 120},
        {"label": "Weight (kg)",     "fieldname": "current_weight",        "fieldtype": "Float", "width": 120},
        {"label": "Calories",        "fieldname": "daily_calorie_intake",  "fieldtype": "Float", "width": 120},
        {"label": "BMI",             "fieldname": "bmi",                   "fieldtype": "Float", "width":  80},
    ]

    # 3) Message (optional)
    message = None

    # 4) Chart: Safe float conversion with fallback
    valid = [r for r in data if r.date]
    chart = {
        "data": {
            "labels": [r.date.strftime("%Y-%m-%d") for r in valid],
            "datasets": [
                {
                    "name": "Weight (kg)",
                    "values": [float(r.current_weight) if r.current_weight is not None else 0 for r in valid]
                },
                {
                    "name": "Calories",
                    "values": [float(r.daily_calorie_intake) if r.daily_calorie_intake is not None else 0 for r in valid]
                },
                {
                    "name": "BMI",
                    "values": [float(r.bmi) if r.bmi is not None else 0 for r in valid]
                },
            ]
        },
        "type": "line",
        "colors": ["#f97316", "#10b981", "#3b82f6"],
        "height": 300
    }

    return columns, data, message, chart
