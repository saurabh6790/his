# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.mapper import get_mapped_doc
from frappe.model.document import Document

class CaseStudy(Document):
	def on_submit(self):
		self.set_status("Submitted")

	def on_cancel(self):
		self.set_status("Cancelled")

	def set_status(self, status):
		self.db_set("status", status)

def update_status(doc, method):
	for data in doc.items:
		if data.case_study:
			status = 'Billed' if doc.docstatus == 1 else 'Submitted'
			case_study_doc = frappe.get_doc("Case Study", data.case_study)
			case_study_doc.set_status(status)

@frappe.whitelist()
def make_sales_invoice(source_name, target_doc=None):
	def postprocess(source, target):
		set_missing_values(source, target)
		target.set_advances()

	def set_missing_values(source, target):
		target.is_pos = 0
		target.ignore_pricing_rule = 1
		target.flags.ignore_permissions = True
		target.run_method("set_missing_values")
		target.run_method("calculate_taxes_and_totals")

	doclist = get_mapped_doc("Case Study", source_name, {
		"Case Study": {
			"doctype": "Sales Invoice",
			"field_map": {
				"patient": "customer",
				"patient_name": "customer_name",
				"name":"case_study"
			},
			"validation": {
				"docstatus": ["=", 1]
			}
		},
		"Test Detail": {
			"doctype": "Sales Invoice Item",
			"field_map": {
				"test": "item_code",
				"test_name": "item_name",
				"parent": "case_study"
			},
		}
	}, target_doc, postprocess)
	
	return doclist
	