from django.http import HttpResponse
from django.shortcuts import render, redirect
from Client.models import client
from pymsgbox import *

# Create your views here.
def home_view(request):
	return render(request, "view.html", {})

def signin_view(request):

	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')

		try:
			q1 = client.objects.get(email=email)

		except Exception as e:
			alert(text='Invalid Email ID', title='Error', button='OK')
			return redirect('/signin/')
		else:
			if q1.password==password:
				print('Login Success')
				return redirect('/')
			else:
				alert(text='Invalid Password', title='Error', button='OK')
				return redirect('/signin/')
			
	else:
		return render(request, "login.html", {})