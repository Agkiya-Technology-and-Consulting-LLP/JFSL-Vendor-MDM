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
        if( turnover ==="<2000000"){
            frm.set_value('gst_status',"Unregistered")
        }
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
            frappe.call({
                method: 'get_user_list',
                doc: frm.doc,
                callback: function(response) {
                    if (response.message) {
                        const userList = response.message;
                        const userNames = userList.map(user => user.name);
    
                        frm.set_query("l1_manager", function() {
                            return {
                                filters: {
                                    name: ["in", userNames]
                                }
                            };
                        });
                    }
                }
            });
        // }
        frm.add_custom_button(__("Check List"), () => {
            var url=''
            frappe.call({
                method: 'frappe.client.get_value',
                args: {
                doctype: 'Configuration',
                name: "Configuration",
                fieldname: 'check_list_url'
                },
                   callback: function(r){	
                    url =r.message.check_list_url					
                      
                       console.log(r,window.origin);
                       var openlink = window.open(window.origin+ url)
                }
            });
            
        })

        if((frm.doc.workflow_state=='Approval Pending By MDM Manager')&& !frm.doc.mdm_manager_check){
	        frm.set_intro(__("Please Check MDM Manager Check for further processing."));
	        
	        function jumpToMoreInfoTab() {
                var moreInfoTab = $('#supplier-clone-viewed_by_tab-tab');
                console.log("More Info Tab Element:", moreInfoTab);
    
                if (moreInfoTab.length) {
                    console.log("More Info Tab found");
                    moreInfoTab.click();  // Trigger click event
                    
                    // Manually switch tab using Bootstrap tab methods if click does not work
                    var tabId = moreInfoTab.attr('href'); // Get the tab pane id
                    $('.tab-pane').removeClass('active show'); // Hide all tab panes
                    $(tabId).addClass('active show'); // Show the target tab pane
                    moreInfoTab.tab('show'); // Bootstrap tab method
                    
                    document.querySelectorAll("[data-fieldname='mdm_manager_check']").forEach(function(element) {
                        const label = element.querySelector(".label-area");
                        if (label) {
                            label.style.backgroundColor = 'yellow';
                        }
                    });
                    console.log("Jumped to More Info tab");
                } else {
                    console.log("More Info tab not found");
                }
            }
    
            // Use a delay to ensure the tab is ready
            setTimeout(function() {
                    jumpToMoreInfoTab();
                }, 100); // Adjust the delay time as needed
    	   }
    },
    onload(frm) {
        if(frappe.session.user !='Administrator'){
        // if(frm.doc.company_user){
        //     if (frappe.session.user !== frm.doc.company_user && frm.doc.company_user_check && (frm.doc.workflow_state=='Approval Pending By Company User Team'|| frm.doc.workflow_state=='Pushed Back By L1 Manager')) {
                
        //         frappe.throw(__("Warning: This form was viewed by a another user ({0})", [frm.doc.company_user]));
        //     }
        // }
        // if (frm.doc.l1_manager){
        //     if (frappe.session.user !== frm.doc.l1_manager && frm.doc.l1_manager_check && (frm.doc.workflow_state=='Approval Pending By L1 Manager')) {
                
        //         frappe.throw(__("Warning: This form was viewed by a another user ({0})", [frm.doc.l1_manager]));
        //     }
        // }
        if(frm.doc.mdm_manager){
            if (frappe.session.user !== frm.doc.mdm_manager && frm.doc.mdm_manager_check && (frm.doc.workflow_state=='Approval Pending By MDM Manager')) {
                
                frappe.throw(__("Warning: This form was viewed by a another user ({0})", [frm.doc.mdm_manager]));
            }
        }
    }
    },
    validate(frm) {
        if(frappe.session.user !='Administrator'){
        // if(frm.doc.company_user){
        //     if (frappe.session.user !== frm.doc.company_user && (frm.doc.company_user_check && frm.doc.workflow_state=='Approval Pending By Company User Team'|| frm.doc.workflow_state=='Pushed Back By L1 Manager')) {
        //         frappe.throw(__("This form was already viewed by a different user ({0})", [frm.doc.company_user]));
        //     }
        // }
        // if(frm.doc.l1_manager){
        //     if (frappe.session.user !== frm.doc.l1_manager && (frm.doc.l1_manager_check && frm.doc.workflow_state=='Approval Pending By L1 Manager')) {
        //         frappe.throw(__("This form was already viewed by a different user ({0})", [frm.doc.l1_manager]));
        //     }
        // }
        if(frm.doc.mdm_manager){
            if (frappe.session.user !== frm.doc.mdm_manager && (frm.doc.mdm_manager_check && frm.doc.workflow_state=='Approval Pending By MDM Manager')) {
                frappe.throw(__("This form was already viewed by a different user ({0})", [frm.doc.mdm_manager]));
            }
        }
        }
    },
    mdm_manager_check(frm){
	    if(frm.doc.mdm_manager_check==0){
	        frappe.model.set_value(frm.doc.doctype,frm.doc.name,"mdm_manager",null)
	    }
	}
});
