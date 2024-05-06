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
from frappe.model import docfield



class SupplierClone(Document):     

    def validate(self):            
        if self.resistration_date_cst and getdate(self.resistration_date_cst) > getdate():
            frappe.throw("Registration Date for CST Number cannot be greater than today's date.")
        

        if self.registration_date_lst and getdate(self.registration_date_lst) > getdate():
            frappe.throw("Registration Date for LST Number cannot be greater than today's date.")     

        if self.pincode:
            if not (self.pincode.isdigit() and len(self.pincode) == 6):
                frappe.throw("Pincode must be a 6-digit number.")

        if self.gst_valid_from and getdate(self.gst_valid_from) > getdate():
            frappe.throw("GST Valid From date cannot be greater than today's date.")

        if self.gst_status_valid_from and getdate(self.gst_status_valid_from) > getdate():
            frappe.throw("GST Status Valid From date cannot be greater than today's date.")         
        if self.d_b_n_d_i_number:
            if not self.d_b_n_d_i_number.isdigit():
                frappe.throw(_("D & B-N-D-I Number must contain only numbers."))
                
        ########################## gst registration number #####################################################
    
        ###########################  region, city ##########################################################

        #########################################################################################################
		
        if self.company_registration_number:
            alphanumeric_regex = re.compile(r'^(?=.*[a-zA-Z])(?=.*[0-9])[a-zA-Z0-9]*$')
        
            if not alphanumeric_regex.match(self.company_registration_number):
                frappe.throw("Company Registration Number must contain both alphabets and numbers.")
        
        if len(self.company_name) <= 5:
            frappe.throw(("Company Name must be more than 5 characters."))

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


        current_workflow_state = self.workflow_state
        old_workflow_state = frappe.db.get_value("Supplier Clone",self.name,'workflow_state')
        if ((old_workflow_state == "Approval Pending By MDM Manager" and current_workflow_state == "Pushed Back By MDM Manager")):
            self.push_back_by_mdm_manager = frappe.session.user
        
        if ((old_workflow_state == "Approval Pending By MDM Manager" and current_workflow_state == "Pushed Back By MDM Manager")):
            if ((not self.reason_by_mdm_manager)):
                frappe.throw("Reason By MDM manager field is mandatory for MDM manager to fill before sending back the doc.")
        elif ((old_workflow_state == "Approval Pending By L1 Manager" and current_workflow_state == "Pushed Back By L1 Manager")):
            if((not self.reason_by_l1_manager)):
                frappe.throw("Reason By L1 Manager field is mandatory for L1 manager to fill before sending back the doc.")
        elif ((old_workflow_state == "Pushed Back By L1 Manager" and current_workflow_state == "Saved")
            or (old_workflow_state == "Approval Pending By Company User Team" and current_workflow_state == "Saved")
            or (old_workflow_state == "Pushed Back By MDM Manager" and current_workflow_state == "Saved")):
            if((not self.reason_by_company_user_team)):
                frappe.throw("Reason By Company User Team field is mandatory for Company User Team to fill before sending back the doc.")   

        # Freez Window for multiple users
        if frappe.session.user!='Administrator':
            if self.company_user_check and ("Company User Team" in frappe.get_roles()):
                self.company_user=frappe.session.user
            if self.l1_manager_check and ("L1 Manager" in frappe.get_roles()):
                self.l1_manager=frappe.session.user
            if self.mdm_manager_check and ("MDM Manager" in frappe.get_roles()):
                self.mdm_manager=frappe.session.user


            if not self.company_user_check and self.workflow_state=='Approval Pending By L1 Manager':
                frappe.throw("Please Check Company User Check")
            if not self.l1_manager_check and self.workflow_state =='Approval Pending By MDM Manager':
                frappe.throw("Please Check L1 Manager Check")
            if not self.mdm_manager_check and self.workflow_state =='Approved':
                frappe.throw("Please Check MDM Manager Check ")
