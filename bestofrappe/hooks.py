from . import __version__ as app_version

app_name = "bestofrappe"
app_title = "Bestofrappe"
app_publisher = "Mahemudhusain K Manusiya"
app_description = "Theme Customization"
app_email = "mahemudmanusiya52@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/bestofrappe/css/custom5.css"
# app_include_js = "/assets/bestofrappe/js/bestofrappe.js"

# include js, css files in header of web template
# web_include_css = "/assets/bestofrappe/css/bestofrappe.css"
# web_include_js = "/assets/bestofrappe/js/bestofrappe.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "bestofrappe/public/scss/website"

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

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "bestofrappe.utils.jinja_methods",
#	"filters": "bestofrappe.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "bestofrappe.install.before_install"
# after_install = "bestofrappe.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "bestofrappe.uninstall.before_uninstall"
# after_uninstall = "bestofrappe.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bestofrappe.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"bestofrappe.tasks.all"
#	],
#	"daily": [
#		"bestofrappe.tasks.daily"
#	],
#	"hourly": [
#		"bestofrappe.tasks.hourly"
#	],
#	"weekly": [
#		"bestofrappe.tasks.weekly"
#	],
#	"monthly": [
#		"bestofrappe.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "bestofrappe.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "bestofrappe.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "bestofrappe.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["bestofrappe.utils.before_request"]
# after_request = ["bestofrappe.utils.after_request"]

# Job Events
# ----------
# before_job = ["bestofrappe.utils.before_job"]
# after_job = ["bestofrappe.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"bestofrappe.auth.validate"
# ]
