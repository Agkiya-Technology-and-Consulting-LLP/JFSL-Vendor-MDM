# Copyright (c) 2024, krutika@agkiya.com and contributors
# For license information, please see license.txt

from http import client
import frappe
from frappe.model.document import Document
import random
import smtplib
from email.message import EmailMessage
# from twilio.rest import Client


class OTPAuthentication(Document):
    pass
	# def before_insert(self):
	# 	# self.ignore_permissions = True
	# 	otp=''.join([str(random.randint(0, 9)) for _ in range(6)])
	# 	if self.email:
	# 		server =smtplib.SMTP('smtp.gmail.com',587)
	# 		server.starttls()

	# 		from_='krutikawadgaonkar2702@gmail.com'
	# 		server.login(from_,'eorv iafz jhpm jhyv')
			
	# 		msg=EmailMessage()
	# 		msg['Subject']= "Verify OTP"
	# 		msg['From']=from_
	# 		msg['To']=self.email
	# 		msg.set_content("OTP for account varification is \n "+ otp)

	# 		server.send_message(msg)
	# 		self.email_otp=otp
	# 	if self.mobile:
	# 		account_sid = "AC018938439c1b5945e6eb9800f786f6b7"
	# 		auth_token = "dfcd6918630b865eaffcd82539e4f8f9"
	# 		twilio_phone_number = "+18312695811"
	# 		client = Client(account_sid, auth_token)
	# 		message = client.messages.create(
	# 		body=f"Your OTP for mobile number verification is: {otp}",
	# 		from_=twilio_phone_number,
	# 		to=self.mobile
    # 		)
	# 		self.mobile_otp=otp
