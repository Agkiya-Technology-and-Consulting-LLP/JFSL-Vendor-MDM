# Copyright (c) 2024, krutika@agkiya.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class SupplierRegistrationLink(Document):
    def validate(self):
        if not self.user_email:
            self.user_email= frappe.session.user
            
    # def on_submit(self):
    
    def on_submit(self):
        self.create_user()

    def create_user(self):
    # Check if a user with the same email already exists
        if not frappe.db.exists("User", {"email": self.supplier_email}):
        # Create a new user document
            new_user = frappe.get_doc({
                'doctype': 'User',
                'first_name': self.supplier_name,
                'email': self.supplier_email,
                'enabled': 1,  # Enable the user
                'roles': [{
                    'role': 'guest_Supplier'  # Assign the guest_Supplier role
                }]
            })
            new_user.insert(ignore_permissions=True)

            
            # Insert the new user into the database
           
            
        else:
            frappe.msgprint(f"A user with email {self.supplier_email} already exists.", alert=True)

            # frappe.db.commit()  # Commit the transaction to save changes
            # exists=frappe.db.exists("Supplier Clone",{'supplier_email_id':self.supplier_email})
            # if exists:
            #     frappe.throw("Supplier already exists")
            # else:    
        new_supplier = frappe.new_doc('Supplier Clone')
        new_supplier.update({
                'company_name' : self.supplier_name ,
                'supplier_email_id' : self.supplier_email,
                'company_user' : frappe.session.user
		})
        new_supplier.insert(ignore_permissions=True)
        frappe.msgprint("Supplier Created")
        frappe.db.commit()
    # def send_email_to_supplier(doc, method):
    #     if method == "on_submit":
    #         supplier_name = doc.supplier_name
    #         supplier_email = doc.supplier_email
    #         subject = "Registration Confirmation"
    #         message = f"Dear {supplier_name},\n\nYour registration has been confirmed.\n\nThank you,\nYour Company Name"
    #         frappe.sendmail(recipients=[supplier_email], subject=subject, message=message)