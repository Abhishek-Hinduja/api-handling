import frappe

@frappe.whitelist()
def get_name_of_the_user():
    return "hello world"