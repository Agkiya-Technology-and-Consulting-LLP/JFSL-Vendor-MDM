import frappe

@frappe.whitelist(allow_guest = True)
def new(doc):
    print(doc)

    new_doc=frappe.new_doc("OTP Authentication")
    new_doc.update(doc)
    new_doc.insert(ignore_permissions=True)
    return new_doc


@frappe.whitelist(allow_guest = True)
def new_user(doc):
    new_doc=frappe.new_doc("User")
    new_doc.update(doc)
    new_doc.insert(ignore_permissions=True)
    return new_doc
