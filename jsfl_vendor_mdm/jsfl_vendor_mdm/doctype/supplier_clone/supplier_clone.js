// Copyright (c) 2024, krutika@agkiya.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Supplier Clone', {
	company_turnover: function(frm) {
        var turnover = frm.doc.company_turnover; 
        var company_size ;
        if (turnover === '>250000000') {
            company_size = 'Large Scale';
        } else if (turnover === '>100000000') {
            company_size = 'Mid Scale';
        } else if (turnover === '>50000000') {
            company_size = 'Small Scale';
        } else {
            company_size = 'Micro';
        }
        frm.set_value('company_size', company_size);
    },

    company_size: function(frm) {
        var size = frm.doc.company_size; 
        var turnover ;
        if (size === 'Large Scale') {
            turnover = '>250000000';
        } else if (size === 'Mid Scale') {
            turnover = '>100000000';
        } else if (size === 'Small Scale') {
            turnover = '>50000000';
        } else {
            turnover = '<50000000';
        }
        frm.set_value('company_turnover', turnover);
    },
    
    company_name: function(frm) {
        if (frm.doc.company_name) {
            frm.set_value('name_', frm.doc.company_name);
        }
    },

    refresh(frm) {
        // Your code here that runs when the form is refreshed
    },
    onload(frm) {
        if(frappe.session.user !='Administrator'){
        if(frm.doc.company_user){
            if (frappe.session.user !== frm.doc.company_user && frm.doc.company_user_check && (frm.doc.workflow_state=='Approval Pending By Company User Team'|| frm.doc.workflow_state=='Pushed Back By L1 Manager')) {
                
                frappe.throw(__("Warning: This form was viewed by a another user ({0})", [frm.doc.company_user]));
            }
        }
        if (frm.doc.l1_manager){
            if (frappe.session.user !== frm.doc.l1_manager && frm.doc.l1_manager_check && (frm.doc.workflow_state=='Approval Pending By L1 Manager')) {
                
                frappe.throw(__("Warning: This form was viewed by a another user ({0})", [frm.doc.l1_manager]));
            }
        }
        if(frm.doc.mdm_manager){
            if (frappe.session.user !== frm.doc.mdm_manager && frm.doc.mdm_manager_check && (frm.doc.workflow_state=='Approval Pending By MDM Manager')) {
                
                frappe.throw(__("Warning: This form was viewed by a another user ({0})", [frm.doc.mdm_manager]));
            }
        }
    }
    },
    validate(frm) {
        if(frappe.session.user !='Administrator'){
        if(frm.doc.company_user){
            if (frappe.session.user !== frm.doc.company_user && (frm.doc.company_user_check && frm.doc.workflow_state=='Approval Pending By Company User Team'|| frm.doc.workflow_state=='Pushed Back By L1 Manager')) {
                frappe.throw(__("This form was already viewed by a different user ({0})", [frm.doc.company_user]));
            }
        }
        if(frm.doc.l1_manager){
            if (frappe.session.user !== frm.doc.l1_manager && (frm.doc.l1_manager_check && frm.doc.workflow_state=='Approval Pending By L1 Manager')) {
                frappe.throw(__("This form was already viewed by a different user ({0})", [frm.doc.l1_manager]));
            }
        }
        if(frm.doc.mdm_manager){
            if (frappe.session.user !== frm.doc.mdm_manager && (frm.doc.mdm_manager_check && frm.doc.workflow_state=='Approval Pending By MDM Manager')) {
                frappe.throw(__("This form was already viewed by a different user ({0})", [frm.doc.mdm_manager]));
            }
        }
        }
    }
});
