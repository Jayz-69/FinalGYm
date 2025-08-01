app_name = "gym_management"
app_title = "Jim"
app_publisher = "Jayz"
app_description = "Gym-management System"
app_email = "jay.anjarlekar@cloverinfotech.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "gym_management",
# 		"logo": "/assets/gym_management/logo.png",
# 		"title": "Jim",
# 		"route": "/gym_management",
# 		"has_permission": "gym_management.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gym_management/css/gym_management.css"
# app_include_js = "/assets/gym_management/js/gym_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/gym_management/css/gym_management.css"
# web_include_js = "/assets/gym_management/js/gym_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "gym_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "gym_management/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "gym_management.utils.jinja_methods",
# 	"filters": "gym_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "gym_management.install.before_install"
# after_install = "gym_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "gym_management.uninstall.before_uninstall"
# after_uninstall = "gym_management.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "gym_management.utils.before_app_install"
# after_app_install = "gym_management.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "gym_management.utils.before_app_uninstall"
# after_app_uninstall = "gym_management.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gym_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"gym_management.tasks.all"
# 	],
# 	"daily": [
# 		"gym_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"gym_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"gym_management.tasks.weekly"
# 	],
# 	"monthly": [
# 		"gym_management.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "gym_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "gym_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "gym_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["gym_management.utils.before_request"]
# after_request = ["gym_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["gym_management.utils.before_job"]
# after_job = ["gym_management.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"gym_management.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

after_login = "gym_management.utils.redirect_after_login"

# website_include_js = [
#     "public/js/login_redirect.js"
# ]


# permission_query_conditions = {
#     "Gym Membership": "gym_management.jim.doctype.gym_membership.gym_membership.get_permission_query_conditions"
# }

# has_permission = {
#     "Gym Membership": "gym_management.jim.doctype.gym_membership.gym_membership.has_permission"
# }

doc_events = {
    "Gym Membership": {
        "after_submit": "gym_management.jim.doctype.gym_membership.gym_membership.GymMembership.after_submit"
    }
}

website_route_rules = [
{"from_route": "/member-details", "to_route": "member_details"}
]

import gym_management.jim.api

# fixtures = [
#     "Client Script",
#     "Property Setter",
#     "Report",
#     "Web Form",

#     # Your custom DocTypes (with all records)
#     {
#         "doctype": "BMI",
#         "filters": []
#     },
#     {
#         "doctype": "Gym Membership",
#         "filters": []
#     },
#     {
#         "doctype": "Trainer Ratings",
#         "filters": []
#     },
#     {
#         "doctype": "Gym Class Booking",
#         "filters": []
#     },
#     {
#         "doctype": "TrainerReg",
#         "filters": []
#     },
#     {
#         "doctype": "Gym Member",
#         "filters": []
#     },
#     {
#         "doctype": "Gym Workout Plan",
#         "filters": []
#     },
#     {
#         "doctype": "Available Lockers",
#         "filters": []
#     },
#     {
#         "doctype": "Metrics Update",
#         "filters": []
#     },
#     {
#         "doctype": "Gym Settings",
#         "filters": []
#     },
#     {
#         "doctype": "Specializations",
#         "filters": []
#     },

#     # Website-related assets
#     {
#         "doctype": "Web Page",
#         "filters": [["module", "=", "Jim"]]
#     },
#     {
#         "doctype": "Web Template",
#         "filters": [["module", "=", "Jim"]]
#     },
#     {
#         "doctype": "Website Settings",
#         "filters": []
#     }
# ]




fixtures = [
    # Core Frappe Features
    "Client Script",
    "Property Setter",
    "Report",
    "Web Form",

    # Your custom roles (only selected ones)
    {
        "doctype": "Role",
        "filters": [["name", "in", ["Gym Member", "Gym Trainer", "Gym Admin"]]]
    },
    {
        "doctype": "Custom DocPerm",
        "filters": [["role", "in", ["Gym Member", "Gym Trainer", "Gym Admin"]]]
    },

    # Website-related assets (optional)
    {
        "doctype": "Web Page",
        "filters": [["module", "=", "Jim"]]
    },
    {
        "doctype": "Web Template",
        "filters": [["module", "=", "Jim"]]
    },
    {
        "doctype": "Website Settings",
        "filters": []
    }
]
