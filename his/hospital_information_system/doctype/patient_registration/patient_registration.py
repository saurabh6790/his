# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import nowdate
from frappe import _

class PatientRegistration(Document):
	def validate(self):
		self.create_customer()
		self.create_user()

	def create_customer(self):
		if not frappe.db.exists("Customer", self.name):
			customer = frappe.get_doc({
				"doctype": "Customer",
				"customer_name": self.patient_name,
				"name": self.name,
				"territory": _("All Territories"),
				"customer_group": "Patient",
				"customer_type": "Individual"
			})
			
			customer.flags.patient_name = self.name
			customer.flags.ignore_madatory=True
			customer.insert(ignore_permissions=True)
	
	def create_user(self):
		user_email = self.email if self.email else "{0}.{1}".format(self.mobile, frappe.db.get_value("HIS Settings", None, "default_domain"))
		if not frappe.db.exists("User", user_email):
			user = frappe.get_doc({
				"doctype": "User",
				"email": user_email,
				"first_name": self.patient_name
			})

			user.flags.ignore_madatory=True
			user.insert(ignore_permissions=True)
			

def set_customer_name(doc, method):
	if doc.flags.patient_name:
		doc.name = doc.flags.patient_name
		
@frappe.whitelist()
def make_advance_payment_entry(party, amount):
	company = frappe.db.get_value("Global Defaults", None, "default_company")
	company_data = frappe.db.get_value("Company", company, ["default_receivable_account", "default_cash_account"], as_dict=1)
	
	je = frappe.get_doc({
		"doctype": "Journal Entry",
		"voucher_type": "Journal Entry",
		"posting_date": nowdate(),
		"user_remark": "Advance payment entry against patient id {0}".format(party),
		"accounts": [{
				"account": company_data.default_receivable_account,
				"party_type": "Customer",
				"party": party,
				"credit_in_account_currency": amount,
				"is_advance": "Yes"
			},
			{
				"account": company_data.default_cash_account,
				"debit_in_account_currency": amount
			}
		]
	}).insert(ignore_permissions = True)
	je.submit()