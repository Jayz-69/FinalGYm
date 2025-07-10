import frappe

def execute(filters=None):
    member = filters.get("member")

    if not isinstance(member, str) or not member:
        frappe.throw("Please select a valid member.")

    # Step 1: Fetch fitness data from child table Metrics Update (of BMI)
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
            b.name = %s
        ORDER BY
            m.date ASC
    """, (member,), as_dict=True)

    # Step 2: Define table columns
    columns = [
        {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 120},
        {"label": "Weight (kg)", "fieldname": "current_weight", "fieldtype": "Float", "width": 120},
        {"label": "Height (cm)", "fieldname": "current_height", "fieldtype": "Float", "width": 120},
        {"label": "Daily Calories", "fieldname": "daily_calorie_intake", "fieldtype": "Int", "width": 140},
        {"label": "BMI", "fieldname": "bmi", "fieldtype": "Float", "width": 100},
    ]

    # Step 3: Define line chart for trend visualization
    chart = {
        "data": {
            "labels": [d["date"].strftime("%Y-%m-%d") for d in data],
            "datasets": [
                {
                    "name": "Weight (kg)",
                    "values": [d["current_weight"] for d in data]
                },
                {
                    "name": "Calories",
                    "values": [d["daily_calorie_intake"] for d in data]
                },
                {
                    "name": "BMI",
                    "values": [d["bmi"] for d in data]
                },
            ]
        },
        "type": "line",  # or "bar", "pie", etc.
        "colors": ["#36a2eb", "#ff6384", "#4caf50"]
    }

    return columns, data, None, chart
