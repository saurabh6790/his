# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "his"
app_title = "Hospital Information System"
app_publisher = "Frappe Technologies Pvt Ltd"
app_description = "Hospital Information System"
app_icon = "octicon octicon-plus"
app_color = "#bf0808"
app_email = "info@erpnext.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/his/css/his.css"
# app_include_js = "/assets/his/js/his.js"

# include js, css files in header of web template
# web_include_css = "/assets/his/css/his.css"
# web_include_js = "/assets/his/js/his.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "his.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "his.install.before_install"
# after_install = "his.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "his.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Customer": {
		"autoname": "his.hospital_information_system.doctype.patient_registration.patient_registration.set_customer_name"
	},
	"Sales Invoice": {
		"on_submit": "his.hospital_information_system.doctype.case_study.case_study.update_status",
		"on_cancel": "his.hospital_information_system.doctype.case_study.case_study.update_status"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"his.tasks.all"
# 	],
# 	"daily": [
# 		"his.tasks.daily"
# 	],
# 	"hourly": [
# 		"his.tasks.hourly"
# 	],
# 	"weekly": [
# 		"his.tasks.weekly"
# 	]
# 	"monthly": [
# 		"his.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "his.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "his.event.get_events"
# }


fixtures = ["Role", "Custom Field"]