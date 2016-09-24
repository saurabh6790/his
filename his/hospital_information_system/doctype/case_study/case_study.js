// Copyright (c) 2016, Frappe Technologies Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Case Study', {
	refresh: function(frm) {
		if(frm.doc.docstatus == 1){
			frm.add_custom_button("Make Bill", function(){
				frm.trigger("make_invoice")
			})
		}
	},
	
	make_invoice: function(frm) {
		frappe.model.open_mapped_doc({
			method: "his.hospital_information_system.doctype.case_study.case_study.make_sales_invoice",
			frm: frm
		});
	},
});
