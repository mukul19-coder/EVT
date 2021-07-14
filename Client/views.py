from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages	
from django.contrib.auth.models import User, auth

import random
import math

from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings



OTP = "Null"
user = "Null"
"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""
def generateOTP() :
  
    # Declare a digits variable  
    # which stores all digits 
    digits = "0123456789"
    global OTP
    OTP = ""
  
   # length of password can be chaged
   # by changing value in range
    for i in range(6) :
        OTP += digits[math.floor(random.random() * 10)]
  
    return OTP

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def signup_view(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		#oname = request.POST['oname']
		#number = request.POST['number']
		#address = request.POST['address']

		if password1 == password2:
			if User.objects.filter(email=email).exists():
				messages.info(request,'EMAIL ALREADY IN USE')
				return render(request, "signup.html", {})
			else:
				global user
				user = User.objects.create_user(username=email, password=password1, email=email, first_name=first_name, last_name=last_name, is_active=False)
				user.save();

				html_tpl_path = 'otp.html'
				context_data = {'otp':generateOTP()}
				email_html_template = get_template(html_tpl_path).render(context_data)
				receiver_mail = email
				email_msg = EmailMessage('Email Verification', email_html_template, settings. APPLICATION_EMAIL, [receiver_mail], reply_to=[settings.APPLICATION_EMAIL])
				email_msg.content_subtype = 'html'
				email_msg.send(fail_silently=False)

				return render(request, "verification.html", {'u':user})

		else:
			messages.info(request,'PASSWORD DO NOT MATCH')
			return render(request, "signup.html", {})

	else:
		return render(request, 'signup.html')



def verification(request):
	if request.method == 'POST':
		otp = request.POST['OTP']

		if OTP == otp:
			u = User.objects.get(username =user.username)
			u.is_active = True
			u.save();
			html_tpl_path = 'welcome.html'
			context_data = {'c':user}
			email_html_template = get_template(html_tpl_path).render(context_data)
			receiver_mail = user.email
			email_msg = EmailMessage('WELCOME TO EVT', email_html_template, settings. APPLICATION_EMAIL, [receiver_mail], reply_to=[settings.APPLICATION_EMAIL])
			email_msg.content_subtype = 'html'
			email_msg.send(fail_silently=False)
			return redirect('/')

		else:
			messages.info(request, 'INVALID OTP')
			return redirect('/verification/')

	else:
		return render(request, 'verification.html')
	