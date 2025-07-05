# most_popular_group_classes.py

import frappe

def execute(filters=None):
    columns = [
        {
            "label": "Specialization",
            "fieldname": "specialization",
            "fieldtype": "Link",
            "options": "Specializations",
            "width": 250
        },
        {
            "label": "Total Memberships",
            "fieldname": "total",
            "fieldtype": "Int",
            "width": 150
        }
    ]

    data = frappe.db.sql("""
        SELECT 
            specialization, 
            COUNT(*) as total
        FROM `tabGym Membership`
        WHERE specialization IS NOT NULL
            AND docstatus < 2  -- includes 0 (Draft) and 1 (Submitted)
            AND status != 'Cancelled'
        GROUP BY specialization
        ORDER BY total DESC
    """, as_dict=True)

    chart = {
        "data": {
            "labels": [row["specialization"] for row in data],
            "datasets": [
                {
                    "name": "Total Memberships",
                    "values": [row["total"] for row in data]
                }
            ]
        },
        "type": "bar"  # or "pie", "line"
    }

    return columns, data, None, chart
