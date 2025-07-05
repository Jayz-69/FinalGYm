// Copyright (c) 2025, Jayz and contributors
// For license information, please see license.txt

frappe.query_reports["Fitness Journey Report"] = {
    "filters": [
        {
            "fieldname": "member",
            "label": "Gym Member",
            "fieldtype": "Link",
            "options": "User",
            "reqd": 1
        }
    ]
};
