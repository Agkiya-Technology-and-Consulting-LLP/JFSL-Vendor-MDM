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
        if self.company_name and not self.supplier_name:
            self.supplier_name =self.company_name

        if self.account_number:
            if not self.confirm_account_number:
                frappe.throw("Confirm Account Number field is mandatory if Account Number is provided.")
            elif self.account_number != self.confirm_account_number:
                frappe.throw("Account Number and Confirm Account Number fields should be the same.")

        
        # elif self.supplier_name and not self.company_name:
        #     self.supplier_name =self.company_name
        # if self.gst_status_valid_from and getdate(self.gst_status_valid_from) > getdate():
        #     frappe.throw("GST Status Valid From date cannot be greater than today's date.")         
        # if self.d_b_n_d_i_number:
        #     if not self.d_b_n_d_i_number.isdigit():
        #         frappe.throw(_("D & B-N-D-I Number must contain only numbers."))
                
        ########################## gst registration number #####################################################
    
        ###########################  region, city ##########################################################

        #########################################################################################################
		
        if self.company_registration_number:
            alphanumeric_regex = re.compile(r'^(?=.*[a-zA-Z])(?=.*[0-9])[a-zA-Z0-9]*$')
        
            if not alphanumeric_regex.match(self.company_registration_number):
                frappe.throw("Company Registration Number must contain both alphabets and numbers.")
        
        # if len(self.company_name) <= 5:
        #     frappe.throw(("Company Name must be more than 5 characters."))

        if self.date_of_establishment and getdate(self.date_of_establishment) > getdate():
            frappe.throw("Date of establishment cannot be greater than today's date.")  
        
        # if self.sent_back_by:
        #     current_workflow_state = self.workflow_state
        #     old_workflow_state = frappe.db.get_value("Supplier Clone",self.name,'workflow_state')
        #     if((old_workflow_state == "Approval Pending By MDM Manager" and current_workflow_state == "Approval Pending By L1 Manager") or(old_workflow_state == "Approval Pending By L1 Manager" and current_workflow_state == "Approval Pending By Company User Team") or (old_workflow_state == "Approval Pending By Company User Team" and current_workflow_state == "Saved")):
        #         self.sent_back_by = frappe.session.user
        #     else:
        #        self.sent_back_by = " " 
        #     # self.sent_back_by = frappe.session.user 
        #     # roles = frappe.get_roles(frappe.session.user)
        #     # roles_string = ",".join(roles)
        #     # frappe.msgprint(roles_string)
        # else:
        #     self.sent_back_by = " "


        current_workflow_state = self.workflow_state
        old_workflow_state = frappe.db.get_value("Supplier Clone",self.name,'workflow_state')
        if (current_workflow_state == "Rejected" and (old_workflow_state == "Approval Pending By MDM Manager" or old_workflow_state == "Approval Pending By L1 Manager" or old_workflow_state == "Approval Pending By Tamalika")):
            if (not self.reason_for_rejection):
                frappe.throw("Rejection Reason is mandetory before rejecting the form")
        if ((old_workflow_state == "Approval Pending By MDM Manager" and current_workflow_state == "Pushed Back By MDM Manager")):
            self.push_back_by_mdm_manager = frappe.session.user
        
        if ((old_workflow_state == "Approval Pending By MDM Manager" and current_workflow_state == "Pushed Back By MDM Manager")):
            if ((not self.reason_by_mdm_manager)):
                frappe.throw("Pushback Reason By MDM manager field is mandatory for MDM manager to fill before sending back the doc.")
        elif ((old_workflow_state == "Approval Pending By L1 Manager" and current_workflow_state == "Pushed Back By L1 Manager")):
            if((not self.reason_by_l1_manager)):
                frappe.throw("Pushback Reason By L1 Manager field is mandatory for L1 manager to fill before sending back the doc.")
        elif ((old_workflow_state == "Pushed Back By L1 Manager" and current_workflow_state == "Saved")
            or (old_workflow_state == "Approval Pending By Company User Team" and current_workflow_state == "Saved")
            or (old_workflow_state == "Pushed Back By MDM Manager" and current_workflow_state == "Saved")
            or (old_workflow_state == "Pushed Back By Tamalika" and current_workflow_state == "Saved")):
            if((not self.reason_by_company_user_team)):
                frappe.throw("Pushback Reason By Company User Team field is mandatory for Company User Team to fill before sending back the doc.")   
        elif ((old_workflow_state == "Approval Pending By Tamalika" and current_workflow_state == "Pushed Back By Tamalika")):
            if ((not self.reason_by_reviewer)):
                frappe.throw("Pushback Reason By Reviewer field is mandatory for Tamalika to fill before sending back the doc.")
        

        # ***********************************************************************************************************************
        # if ((old_workflow_state == "Approval Pending By Company User Team" or old_workflow_state == "Pushed Back By MDM Manager" or old_workflow_state == "Pushed Back By L1 Manager" or old_workflow_state=="Pushed Back By Tamalika") and current_workflow_state == "Saved"):
        # # Retrieve the supplier email
        #     # user_email = frappe.db.get_value("Supplier Clone", self.supplier_email_id, "supplier_email_id")
            
        #     # Debug: Check the retrieved email
        #     # print(f"@@@@@@@@@@@@Retrieved user email:",self.supplier_email_id)
            
        #     if self.supplier_email_id:
        #         try:
        #             # Send email
        #             frappe.sendmail(
        #                 recipients=self.supplier_email_id,
        #                 subject=f"Supplier Registration Form named  {self.name} is returned by User Team",
        #                 content=f"""
        #                     <div style="border: 2px solid #0199aa; padding: 20px; display: inline-block; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); font-family: Arial, sans-serif; background-color: #f9f9f9;">
        #                         <h3 style="margin-top: 0; color: #6a0cc7; text-align: center; text-decoration: underline;">Form named {self.name} has been returned.</h3>
        #                         <p>Dear {self.supplier_name},</p>
        #                         <p>We regret to inform you that your form has been returned by the User Team:</p>
        #                         <p><strong>Reason:</strong> {self.reason_by_company_user_team}</p>
        #                         <p>Please click <a href="https://uat-jfsl-mdm.frappe.cloud/frontend/account/login">THIS LINK</a> to update your information</p>
        #                         <p><strong> Please take necessary action on it.</strong></p>
        #                     </div>
        #                 """
        #             )
        #             frappe.msgprint("Email sent successfully.", alert=True)
        #         except Exception as e:
        #             frappe.throw(f"An error occurred while sending the email: {str(e)}")
        #     else:
        #         frappe.msgprint("No valid email address found for the supplier.", alert=True)

        # ***********************************************************************************************************************


        # Freez Window for multiple users
        if frappe.session.user!='Administrator':
            # if self.company_user_check and ("Company User Team" in frappe.get_roles()):
            #     self.company_user=frappe.session.user
            # if ("L1 Manager" in frappe.get_roles()):
            #     self.l1_manager=frappe.session.user
            if self.mdm_manager_check and ("MDM Manager" in frappe.get_roles()):
                self.mdm_manager=frappe.session.user


            # if not self.company_user_check and self.workflow_state=='Approval Pending By L1 Manager':
            #     frappe.throw("Please Check Company User Check")
            # if not self.l1_manager_check and self.workflow_state =='Approval Pending By MDM Manager':
            #     frappe.throw("Please Check L1 Manager Check")
            if not self.mdm_manager_check and self.workflow_state =='Approved':
                frappe.throw("Please Check MDM Manager Check ")
            if not self.l1_manager and self.workflow_state =='Approval Pending By L1 Manager':
                frappe.throw("Please Select L1 Manager First ")

        
        if self.name:
            old_doc = self.get_doc_before_save()
            # frappe.msgprint(str(old_doc))
            if old_doc and old_doc.workflow_state == "Approved":
                # Check if any field value has changed
                has_changes = False
                for field in self.meta.fields:
                    fieldname = field.fieldname
                    if old_doc.get(fieldname) != self.get(fieldname):
                        has_changes = True
                        break

                if has_changes:
                    self.workflow_state = "Change Requested"
                    # doc.save()
                    frappe.db.commit
                    # frappe.msgprint("Workflow state changed to 'Change Requested' due to changes in the document.")

    def before_insert(self):
        self.timestamp = frappe.utils.now()


    @frappe.whitelist()
    def get_user_list(self):
        # return frappe.db.get_list(
        #     'User',
        #     filters={
        #         'name': ['in', frappe.db.get_list(
        #             'Has Role',
        #             filters={'role': 'L1 Manager'},
        #             pluck='parent'
        #         )]
        #     },
        #     fields=['name', 'full_name']
        # )


        role_user=frappe.db.sql("""
		SELECT 
			u.name 
		from  
			`tabUser` u ,`tabHas Role` hr 
		where  
			hr.parent=u.name 
		and  
			u.enabled=1 and hr.role ='{}'
		""".format("L1 Manager"),as_dict=True,debug=0)
        return role_user
        # return frappe.db.sql("""
                

        #     """)