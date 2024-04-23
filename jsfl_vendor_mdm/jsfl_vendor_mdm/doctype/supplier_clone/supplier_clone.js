// Copyright (c) 2024, krutika@agkiya.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Supplier Clone', {
	company_turnover: function(frm) {
        var turnover = frm.doc.company_turnover; 
        var company_size ;
        if (turnover === '> 250000000') {
            company_size = 'Large Scale';
        } else if (turnover === '> 100000000') {
            company_size = 'Mid Scale';
        } else if (turnover === '> 50000000') {
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
            turnover = '> 250000000';
        } else if (size === 'Mid Scale') {
            turnover = '> 100000000';
        } else if (size === 'Small Scale') {
            turnover = '> 50000000';
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
});
