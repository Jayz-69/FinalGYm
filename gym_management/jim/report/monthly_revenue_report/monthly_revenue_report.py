import frappe

def execute(filters=None):
    # 1) Fetch revenue per month based on start_date
    data = frappe.db.sql("""
        SELECT
            DATE_FORMAT(start_date, '%Y-%m') AS month,
            SUM(final_price) AS total_revenue
        FROM `tabGym Membership`
        WHERE docstatus < 2
        GROUP BY DATE_FORMAT(start_date, '%Y-%m')
        ORDER BY DATE_FORMAT(start_date, '%Y-%m')
    """, as_dict=True)

    # 2) Columns
    columns = [
        {"label": "Month",           "fieldname": "month",         "fieldtype": "Data",     "width": 150},
        {"label": "Total Revenue ₹", "fieldname": "total_revenue", "fieldtype": "Currency", "width": 200},
    ]

    # 3) Optional message
    message = None

    # 4) Chart data
    chart = {
        "data": {
            "labels": [row["month"] for row in data],
            "datasets": [{
                "name": "Total Revenue",
                "values": [row["total_revenue"] for row in data]
            }]
        },
        "type": "bar",
        "colors": ["#36B37E"],
        "height": 300
    }

    # 5) Return all
    return columns, data, message, chart
