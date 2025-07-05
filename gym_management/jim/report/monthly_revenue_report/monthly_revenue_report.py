import frappe

def execute(filters=None):
    # 1) Fetch data, building “YYYY‑MM” manually
    data = frappe.db.sql("""
        SELECT
            CONCAT(
                YEAR(start_date),
                '-',
                LPAD(MONTH(start_date), 2, '0')
            ) AS month,
            SUM(final_price) AS total_revenue
        FROM `tabGym Membership`
        WHERE status = 'Active'
        GROUP BY YEAR(start_date), MONTH(start_date)
        ORDER BY YEAR(start_date), MONTH(start_date)
    """, as_dict=True)

    # 2) Define columns
    columns = [
        {"label": "Month",           "fieldname": "month",         "fieldtype": "Data",     "width": 150},
        {"label": "Total Revenue ₹", "fieldname": "total_revenue", "fieldtype": "Currency", "width": 200},
    ]

    # 3) No extra message
    message = None

    # 4) Build chart
    chart = {
        "data": {
            "labels": [row["month"] for row in data],
            "datasets": [{
                "name":   "Total Revenue",
                "values": [row["total_revenue"] for row in data]
            }]
        },
        "type":   "bar",
        "colors": ["#FF69B4"],
        "height": 300
    }

    # 5) Return all four
    return columns, data, message, chart
