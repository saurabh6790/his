// Copyright (c) 2016, Frappe Technologies Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Patient Registration', {
	refresh: function(frm) {
		frm.add_custom_button(__("View Customer"), function(){
			frappe.set_route("Form", "Customer", frm.doc.name)
		})
		
		frm.add_custom_button(__("Advance Payment"), function(){
			frm.trigger("make_advance_payment")
		}, __("Make"))
		
		frm.add_custom_button(__("Appointment"), function(){
			frm.trigger("make_appointment")
		}, __("Make"))
		
		frm.add_custom_button(__("Case Study"), function(){
			frm.trigger("make_case_study")
		}, __("Make"))
		
		cur_frm.page.set_inner_btn_group_as_primary(__("Make"));
	},

	make_advance_payment: function(frm){
		var dialog = new frappe.ui.Dialog({
			title: __('Advance Payment'),
			fields: [
				{
					fieldtype: "Currency", fieldname: "amount", label: __("Amount"),
					"default": 0.0
				},
			]
		})
		
		dialog.show()
		
		dialog.set_primary_action(__("Make Payment"), function(){
			var d = dialog.get_values()
			if(flt(d.amount) > 0.0){
				frappe.call({
					method: "his.hospital_information_system.doctype.patient_registration.patient_registration.make_advance_payment_entry",
					args: {
						party: frm.doc.name, amount: d.amount
					},
					callback: function(r){
						dialog.hide()
					}
				})
			}
		})
	},

	make_appointment: function(frm){
		frappe.set_route("Calendar", "Event")
	},
	
	make_case_study: function(frm) {
		var doc = frappe.model.get_new_doc('Case Study');
		doc.patient = frm.doc.name
		doc.patient_name = frm.doc.patient_name
		frappe.set_route("Form", "Case Study", doc.name)
	}
 });
