from email.message import EmailMessage
import random
import smtplib
import frappe
from frappe.auth import LoginManager
from frappe.sessions import Session, clear_sessions, delete_session, get_expiry_in_seconds
import requests


@frappe.whitelist(allow_guest = True)
def new(doc):
    new_doc=frappe.new_doc("OTP Authentication")
    new_doc.update(doc)
    new_doc.insert(ignore_permissions=True)
    return new_doc


@frappe.whitelist(allow_guest = True)
def new_user(doc):
    new_doc=frappe.new_doc("User")
    new_doc.update(doc)
    new_doc.append_roles("Guest_supplier")
    new_doc.insert(ignore_permissions=True)
    return new_doc


@frappe.whitelist(allow_guest=True)
def request_verification_code(email):
    user = frappe.get_value("User", {"email": email})
    
    if user:
        verification_code = generate_verification_code()
        send_verification_code(email, verification_code)
        frappe.cache().hset("verification_code", user, verification_code)
        return ("Verification code sent successfully.")
    else:
        return ("Email not found.")

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

@frappe.whitelist(allow_guest=True)
def login(doc):
    user=frappe.get_doc("User",doc['email'])
    print(f"{user.name},{user.full_name},{user.user_type}")
    obj={
        'user':user.name,
        'full_name':user.full_name,
        'user_type':user.user_type
    }
    
    return make_session(obj)

#Login without password
def make_session(obj,resume=False):
    print(f":::{obj['user_type']}:::")
    frappe.local.session_obj = Session(
			user=obj["user"], resume=resume, full_name=obj["full_name"], user_type=obj['user_type']
		)
    obj["user"] = frappe.local.session_obj.user
    frappe.local.session = frappe.local.session_obj.data
    print(frappe.local.session)
    # obj.clear_active_sessions()
    return frappe.local.session.sid


# import frappe
# from frappe import _

@frappe.whitelist(allow_guest=True)
def check(doc):
    try:
        # Log the input doc for debugging
        frappe.logger().debug(f"Received doc: {doc}")

        # Ensure 'doc' is a dictionary and has the 'email' key
        if not isinstance(doc, dict) or 'email' not in doc:
            frappe.throw(_("Invalid document format or missing email"))

        # Check if the user exists
        exists = frappe.db.exists("User", doc['email'])
        frappe.logger().debug(f"User exists: {exists}")

        # Create and insert the new document
        new_doc = frappe.new_doc("OTP Authentication")
        new_doc.update(doc)
        new_doc.insert(ignore_permissions=True)
        
        # Log the new document creation
        frappe.logger().debug(f"New OTP Authentication doc created: {new_doc.name}")

        return new_doc

    except Exception as e:
        # Log the error for debugging
        frappe.logger().error(f"Error in check method: {str(e)}")
        frappe.throw(_("An error occurred while processing the request: ") + str(e))

@frappe.whitelist(allow_guest=True)
def checkUserExists(doc):
    user=frappe.db.exists("User",doc['email'])
    user_doc=frappe.get_doc("User",user)
    return user_doc

@frappe.whitelist(allow_guest=True)
def get_supplier_detail(doc):
    supplier=frappe.get_doc("Supplier Clone",{"supplier_email_id":doc['email']})
    # print(f"<><><><><{supplier}")
    return supplier

@frappe.whitelist(allow_guest=True)
def save_supplier_detail(doc):
    supplier=frappe.get_doc("Supplier Clone",doc['docname'])
    print(f"<><><><><{supplier}")
    supplier.update(doc)
    supplier.save(ignore_permissions=True)
    return supplier

@frappe.whitelist(allow_guest=True)
def submit_supplier_detail(doc):
    supplier=frappe.get_doc("Supplier Clone",doc['docname'])
    supplier.update(doc)
    supplier.save(ignore_permissions=True)
    return supplier

@frappe.whitelist(allow_guest=True)
def accept_code_of_conduct():
    supplier =frappe.new_doc("Supplier Clone")
    supplier.supplier_email_id=frappe.session.user
    supplier.accept_code_of_conduct=1
    supplier.ip_address=get_ip_address()
    supplier.insert(ignore_permissions=True, ignore_mandatory=True)
    return supplier


@frappe.whitelist(allow_guest=True)
def get_bank_details(data):
    try:
        if data['ifscCode']:
            ifscCode = data['ifscCode']
            print(f"oooooooooooooooooooooooooo{ifscCode}")
            response = requests.post(
                'https://testapi.karza.in/v2/ifsc',
                headers={
                    'Content-Type': 'application/json',
                    'x-karza-key': 'lC81SMEYEFlwr24wrjil'  # Replace with your actual API key
                },
                json={'ifsc': ifscCode}  # Include ifsc code in the request body
            )
            print(f"response {response}")
            if response.ok:
                response_data = response.json()
                # Return the JSON response from the external API
                return response_data
            else:
                # Log error message if response is not OK
                error_message = f'Error fetching bank details: {response.status_code}, {response.text}'
                frappe.log_error(error_message)
                return {'message': {'error': 'Error fetching bank details. Please try again later.'}}
        else:
            frappe.logger().error('Missing ifscCode parameter in request data')
            return {'message': {'error': 'Missing ifsc parameter'}}
    
    except Exception as e:
        # Log any exceptions that occur
        error_message = f'Error fetching bank details: {str(e)}'
        # frappe.log_error(error_message)
        # frappe.logger().error(f'Exception: {error_message}')
        print(f".................................................................{e}")
        return {'message': {'error': 'An error occurred while fetching bank details. Please try again later.'}}
    

@frappe.whitelist(allow_guest=True)
def get_pan_details(data):
    if data['pan']:
        response = requests.post(
                'https://testapi.karza.in/v2/pan',
                headers={
                    'Content-Type': 'application/json',
                    'x-karza-key': 'lC81SMEYEFlwr24wrjil'  # Replace with your actual API key
                },
                json={'pan': data['pan'],'consent':'Y'}  # Include ifsc code in the request body
            )
        print(f"********************************{response}")
        if response.ok:
            response_data = response.json()
            print(f'@@@@@@@@@@@@@@@@@@@@@@Response from external API: {response_data}')
            # frappe.logger().info(f'@@@@@@@Response from external API: {response_data}')
            
            # Return the JSON response from the external API
            return response_data
        else:
            # Log error message if response is not OK
            error_message = f'Error fetching PAN details: {response.status_code}, {response.text}'
            frappe.log_error(error_message)
            return {'message': {'error': 'Error fetching PAN details. Please try again later.'}}

# save IP Address       
import socket

def get_ip_address():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Connect to any remote server
        s.connect(('8.8.8.8', 80))

        # Get the local IP address associated with the socket
        ip_address = s.getsockname()[0]

        # Close the socket
        s.close()

        return ip_address
    except socket.error as e:
        print(f"Error: {e}")
        return None

# Get and print the IP address
# ip_address = get_ip_address()

# if ip_address:
#     print(f"Your IP address is: {ip_address}")
# else:
#     print("Unable to retrieve IP address.")