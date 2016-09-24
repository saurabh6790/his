frappe.listview_settings['Case Study'] = {
	add_fields: ["status"],
	get_indicator: function(doc) {
		if (doc.status== "Billed") {
			return [__("Billed"), "green", "status,=," + "Billed"]
		}
	}
};