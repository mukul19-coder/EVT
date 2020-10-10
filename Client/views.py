from django.http import HttpResponse
from django.shortcuts import render, redirect
from Client.models import client

# Create your views here.
def signup_view(request):
	if request.method == 'POST':
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		oname = request.POST.get('oname')
		number = request.POST.get('number')
		address = request.POST.get('address')
		email = request.POST.get('email')
		password = request.POST.get('password')

		user = client(fname=fname, lname=lname, oname=oname, number=number, address=address, email=email, password=password)
		user.save()
		print('user created')
		return redirect('/')
		
	else:
		return render(request, "signup.html", {})

	