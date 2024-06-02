import frappe

def has_permission(doc, user):
    if user == "Administrator" or "System Manager" in frappe.get_roles():
        return True
    elif doc.doctype == "Supplier Clone":
        company=frappe.db.get_value("Employee",{'user_id':user},"company")
        if user == "Administrator" or (("Company User Team" in frappe.get_roles()) and (doc.workflow_state =='Approval Pending By Company User Team' or doc.workflow_state=='Pushed Back By MDM Manager' or doc.workflow_state=='Pushed Back By L1 Manager' or doc.workflow_state =='Approval Pending By L1 Manager' or doc.workflow_state =='Saved' or doc.workflow_state =='Approval Pending By MDM Manager')):
            return True
        elif user == "Administrator" or (("L1 Manager" in frappe.get_roles()) and (doc.workflow_state =='Approval Pending By L1 Manager' or doc.workflow_state=='Pushed Back By L1 Manager' or doc.workflow_state =='Approval Pending By MDM Manager') and doc.l1_manager == user):
            return True
        elif user == "Administrator" or (("MDM Manager" in frappe.get_roles()) and (doc.workflow_state =='Approval Pending By MDM Manager' or doc.workflow_state=='Pushed Back By MDM Manager' or doc.workflow_state == 'Approved')):
            return True
        elif user == "Administrator" or (("Guest_supplier" in frappe.get_roles()) and doc.supplier_email_id == frappe.session.user):
            return True
        else:
            return False
   
    
def get_permission_query_conditions(user):
    if user == "Administrator" or "System Manager" in frappe.get_roles():
        return ""
    else:
        company=frappe.db.get_value("Employee",{'user_id':user},"company")
        if ("Company User Team" in frappe.get_roles()):
            return """(`tabSupplier Clone`.workflow_state = 'Approval Pending By Company User Team' or `tabSupplier Clone`.workflow_state = 'Pushed Back By MDM Manager' or `tabSupplier Clone`.workflow_state = 'Pushed Back By L1 Manager' )"""
        elif ("L1 Manager" in frappe.get_roles()):
            return """(`tabSupplier Clone`.workflow_state = 'Approval Pending By L1 Manager' and `tabSupplier Clone`.l1_manager = '{user}' )""".format(user=user)
        elif ("MDM Manager" in frappe.get_roles()):
            return """(`tabSupplier Clone`.workflow_state = 'Approval Pending By MDM Manager' or `tabSupplier Clone`.workflow_state = 'Approved' )"""
        elif ("Guest_supplier" in frappe.get_roles()):
            return """ (`tabSupplier Clone`.supplier_email_id ='{user}')""".format(user=user)