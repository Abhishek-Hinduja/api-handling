# Copyright (c) 2024, A and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class fullname(Document):
	def validate(self):
		if self.first_name and self.last_name and self.checkbox:
			try:
				self.full_name = f"{self.first_name} {self.last_name}" 
			except Exception as e:
				frappe.msgprint("Exception occured as {e}, what happen")
			
