import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def create_product():
    if frappe.local.request.method != "POST":
        return {"error": "Only POST requests are accepted"}, 405
    data = frappe.local.form_dict

    try:
        user = frappe.get_doc({"doctype":"Product",**data})
        user.insert()
        frappe.db.commit()
        return user.as_dict()
    except Exception as e:
        return {"error": str(e)},500

@frappe.whitelist(allow_guest=True)
def update_product(name,data):
    data = frappe.local.form_dict
    product = frappe.get_doc("Product", "Ballons")

    for key, value in data.items():
        product.set(key, value)

    product.save()
    frappe.db.commit()
    return product.as_dict()

@frappe.whitelist(allow_guest=True)
def get_product(name):
    product = frappe.get_doc("Product", name)
    return product.as_dict()

@frappe.whitelist(allow_guest=True)
def delete_product(name):
    product = frappe.get_doc("Product", name)
    product.delete()
    frappe.db.commit()
    return {"message": _("Product deleted successfully.")}

@frappe.whitelist(allow_guest=True)
def get_users():   
    users = frappe.get_all('User', fields=['name', 'email', 'full_name'])
    return users


@frappe.whitelist(allow_guest=True)
def create_user():
    if(frappe.local.request.method != "POST"):
        return "only POST request is accepted"
    data = frappe.local.form_dict
    try:
        user = frappe.get_doc({"doctype":"User",**data})
        user.insert()
        frappe.db.commit()
        return user.as_dict()
    except Exception as e:
        return {"error": str(e)},500