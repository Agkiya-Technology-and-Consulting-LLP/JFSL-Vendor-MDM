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


@frappe.whitelist(allow_guest=True)
def request_verification_code(email):
    user = frappe.get_value("User", {"email": email})
    
    if user:
        verification_code = generate_verification_code()
        send_verification_code(email, verification_code)
        frappe.cache().hset("verification_code", user, verification_code)
        return _("Verification code sent successfully.")
    else:
        return _("Email not found.")

@frappe.whitelist(allow_guest=True)
def verify_code_and_login(email, verification_code):
    user = frappe.get_value("User", {"email": email})
    stored_code = frappe.cache().hget("verification_code", user)

    if stored_code and stored_code == verification_code:
        try:
            frappe.local.login_manager.login_as(user)
            frappe.local.response["redirect_to"] = "/"
            print("Login successful.")
            return _("Login successful.")
        except Exception as e:
            print(f"Error during login: {e}")
            frappe.local.response["redirect_to"] = "/login"  # Set the redirect path for login failure
            return _("Login failed.")
    else:
        frappe.local.response["redirect_to"] = "/login"  # Set the redirect path for incorrect verification code
        print("Invalid verification code")
        return _("Invalid verification code.")


def generate_verification_code():
    # Implement your code generation logic here (e.g., using random or time-based codes)
    otp=''.join([str(random.randint(0, 9)) for _ in range(6)])
    return otp

def send_verification_code(email, code):
    # Implement code to send the verification code to the user's email
    if email:
        server =smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        from_='krutikawadgaonkar2702@gmail.com'
        server.login(from_,'eorv iafz jhpm jhyv')
        msg=EmailMessage()
        msg['Subject']= "Verify OTP"
        msg['From']=from_
        msg['To']=email
        msg.set_content("OTP for account varification is \n "+ code)
        server.send_message(msg)
        
