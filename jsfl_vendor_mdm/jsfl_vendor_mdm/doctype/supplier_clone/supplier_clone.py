# Copyright (c) 2024, krutika@agkiya.com and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
from datetime import datetime
import re
from frappe import _, throw
from frappe.model.document import Document
from frappe.utils import  getdate
import frappe.workflow




class SupplierClone(Document):     

    def validate(self):
        # Validate Registration Date CST
        if self.resistration_date_cst and getdate(self.resistration_date_cst) > getdate():
            frappe.throw("Registration Date for CST Number cannot be greater than today's date.")
        

         # Validate Registration Date LST
        if self.registration_date_lst and getdate(self.registration_date_lst) > getdate():
            frappe.throw("Registration Date for LST Number cannot be greater than today's date.")     


		#validation for Pincode
        if self.pincode:
            if not (self.pincode.isdigit() and len(self.pincode) == 6):
                frappe.throw("Pincode must be a 6-digit number.")
                

        
        # Check if GST Valid From is greater than today's date
        if self.gst_valid_from and getdate(self.gst_valid_from) > getdate():
            frappe.throw("GST Valid From date cannot be greater than today's date.")
        

        # Check if GST Status Valid From is greater than today's date
        if self.gst_status_valid_from and getdate(self.gst_status_valid_from) > getdate():
            frappe.throw("GST Status Valid From date cannot be greater than today's date.")
                   

        if self.d_b_n_d_i_number:
            # Regular expression to match digits only
            digit_regex = re.compile(r'^\d+$')
            
            # Check if the DBNDI number contains only digits
            if not digit_regex.match(self.d_b_n_d_i_number):
                frappe.throw("D & B-N-D-I Number must contain only numbers.")
        
        ########################## gst registration number #####################################################
        # if self.company_registration_number:
        #     # Regular expression to match alphanumeric characters
        #     alphanumeric_regex = re.compile(r'^[a-zA-Z0-9]*$')
            
        #     # Check if the registration number contains both characters and numbers
        #     if not alphanumeric_regex.match(self.company_registration_number):
        #         frappe.throw("Company Registration Number must contain both characters and numbers.")
    
        ########################### Country, region, city ##########################################################

        #########################################################################################################
		
		# Perform validation only if the company_registration_number field has a value
        if self.company_registration_number:
            # Regular expression to match at least one alphabet and one number
            alphanumeric_regex = re.compile(r'^(?=.*[a-zA-Z])(?=.*[0-9])[a-zA-Z0-9]*$')
            
            # Check if the registration number contains both characters and numbers
            if not alphanumeric_regex.match(self.company_registration_number):
                frappe.throw("Company Registration Number must contain both alphabets and numbers.")
        
		        
        # Validation for Company Name length
        if len(self.company_name) <= 5:
            frappe.throw(("Company Name must be more than 5 characters."))

        #validation for date_of_establishment        
        if self.date_of_establishment and getdate(self.date_of_establishment) > getdate():
            frappe.throw("Date of establishment cannot be greater than today's date.")     


        if self.sent_back_by:
            current_workflow_state = self.workflow_state
            old_workflow_state = frappe.db.get_value("Supplier Clone",self.name,'workflow_state')
            if((old_workflow_state == "Approval Pending By MDM Manager" and current_workflow_state == "Approval Pending By L1 Manager") or(old_workflow_state == "Approval Pending By L1 Manager" and current_workflow_state == "Approval Pending By Company User Team") or (old_workflow_state == "Approval Pending By Company User Team" and current_workflow_state == "Saved")):
                self.sent_back_by = frappe.session.user
            else:
               self.sent_back_by = " " 
            # self.sent_back_by = frappe.session.user 
            # roles = frappe.get_roles(frappe.session.user)
            # roles_string = ",".join(roles)
            # frappe.msgprint(roles_string)
        else:
            self.sent_back_by = " "

        
        
