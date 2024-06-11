import frappe
from frappe import STANDARD_USERS, _, msgprint, throw
from frappe.utils.password import update_password as _update_password
from frappe.utils import (
	cint,
)



def password_reset_mail(self,link):
    print("User custom========================================================================================")
    pass

def send_password_notification(self, new_password):
    if "Guest_supplier" in [user_role.role for user_role in self.get("roles")]: 
        pass
    else:
        try:
            if self.flags.in_insert:
                if self.name not in STANDARD_USERS:
                    if new_password:
                        # new password given, no email required
                        _update_password(
                            user=self.name, pwd=new_password, logout_all_sessions=self.logout_all_sessions
                        )

                    if not self.flags.no_welcome_mail and cint(self.send_welcome_email):
                        self.send_welcome_mail_to_user()
                        self.flags.email_sent = 1
                        if frappe.session.user != "Guest":
                            msgprint(_("Welcome email sent"))
                        return
            else:
                self.email_new_password(new_password)

        except frappe.OutgoingEmailError:
            frappe.clear_last_message()
            frappe.msgprint(
                _("Please setup default outgoing Email Account from Settings > Email Account"), alert=True
            )
            # email server not set, don't send email
            self.log_error("Unable to send new password notification")