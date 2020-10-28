from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages	
from Client.models import client
from .models import cart_1, order_6
from Product.models import elastic, velcro, thread

u = "Null"
content = "Null"
"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def home_view(request):
	return render(request, "view.html", {'c':u})

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def delete_item(request):

	if request.method == 'POST':
		dId = request.POST.get('dId')
		tt = cart_1.objects.get(id=dId)
		tt.delete()
		return redirect('/shoppingcart/')

	else:
		return redirect('/shoppingcart/')

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def shoppingcart_view(request):
	q = u.id
	global content
	content = cart_1.objects.filter(uId=q)
	return render(request, "cart.html", {'c':u, 'con':content})

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def elastic_view(request):
	p = elastic.objects.all()

	if request.method == 'POST':
		pId = request.POST.get('pId')
		qty = request.POST.get('quantity')
		i = elastic.objects.get(id=pId)
		pname = i.name
		uId = u.id
		uo = u.oname
		uname = u.fname
		code = "E"

		item = cart_1(pId=pId, qty=qty, pname=pname, uId=uId, uo=uo, uname=uname, code=code)
		item.save()
		return render(request, "elastic.html", {'elastics':p, 'c':u})

	else:
		return render(request, "elastic.html", {'elastics':p, 'c':u})

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def velcro_view(request):
	v = velcro.objects.all()

	if request.method == 'POST':
		pId = request.POST.get('pId')
		qty = request.POST.get('quantity')
		i = velcro.objects.get(id=pId)
		pname = i.name
		uId = u.id
		uo = u.oname
		uname = u.fname
		code = "V"

		item = cart_1(pId=pId, qty=qty, pname=pname, uId=uId, uo=uo, uname=uname, code=code)
		item.save()
		return render(request, "velcro.html", {'velcros':v, 'c':u})

	else:
		return render(request, "velcro.html", {'velcros':v, 'c':u})

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def thread_view(request):
	t = thread.objects.all()

	if request.method == 'POST':
		pId = request.POST.get('pId')
		qty = request.POST.get('quantity')
		i = thread.objects.get(id=pId)
		pname = i.name
		uId = u.id
		uo = u.oname
		uname = u.fname
		code = "T"

		item = cart_1(pId=pId, qty=qty, pname=pname, uId=uId, uo=uo, uname=uname, code=code)
		item.save()
		return render(request, "thread.html", {'threads':t, 'c':u})

	else:
		return render(request, "thread.html", {'threads':t, 'c':u})

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def log_out(request):
	
	global u
	u= "Null"
	return render(request, "view.html", {'c':u})

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def signin_view(request):

	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')

		try:
			q1 = client.objects.get(email=email)

		except Exception as e:
			messages.info(request,'Invalid Email ID')
			return render(request, "login.html", {})
		else:
			if q1.password==password:
				global u
				u = q1
				print(u)
				return render(request, "view.html", {'c':u})
			else:
				messages.info(request,'Invalid Password')
				return render(request, "login.html", {})
			
	else:
		return render(request, "login.html", {})

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def checkout_view(request):
	e1 = elastic.objects.all()
	v1 = velcro.objects.all()
	t1 = thread.objects.all()
	return render(request, "checkout.html", {'c':u, 'con':content, 'elastics_1':e1, 'velcros_1':v1, 'threads_1':t1})

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def order_1(request):
	if request.method == 'POST':
		uid = u.id
		uname = u.fname
		unumber = u.number
		uorganisationname = u.oname
		uemailaddress = u.email
		uaddress = u.address
		productid = request.POST.get('productid')
		productname = request.POST.get('productname')
		productcode = request.POST.get('productcode')
		productqty = request.POST.get('productqty')
		productamount = request.POST.get('productamount')
		payment = request.POST.get('payment')
		aname = request.POST.get('aname')
		anumber = request.POST.get('anumber')
		bname = request.POST.get('bname')
		transactionid = request.POST.get('tid')
		status = request.POST.get('status')

		purchase = order_6(uid= uid, uname=uname, unumber=unumber, uorganisationname=uorganisationname, uemailaddress=uemailaddress, uaddress=uaddress, productname=productname, productid=productid, productcode=productcode, productqty=productqty, productamount=productamount, payment=payment, aname=aname, anumber=anumber, bname=bname, transactionid=transactionid, status=status)
		purchase.save()
		q1 = content.filter(pId=productid)
		q1.delete()
		return redirect('/elastic/')

	else:
		return redirect('/checkout/')

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def order_view(request):
	o = order_6.objects.all()
	return render(request, "orders.html", {'c':u, 'con':o})