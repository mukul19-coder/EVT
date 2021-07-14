from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages	
from Client.models import Profile
from django.contrib.auth.models import User, auth
from home_view.models import cart_1, order_6
from Product.models import elastic, velcro, thread
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings
import razorpay


u = "Null"
content = "Null"
m1 = "Null"
a1 = "Null"
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

def cancel_order(request):

	if request.method == 'POST':
		cId = request.POST.get('cId')
		tt = order_6.objects.get(id=cId)
		t = Profile.objects.get(user_id=request.user.id)

		html_tpl_path = 'mail1.html'
		context_data = {'c':u, 'profile':t, 'con':tt}
		email_html_template = get_template(html_tpl_path).render(context_data)
		receiver_mail = request.user.email
		email_msg = EmailMessage('Order Canceled', email_html_template, settings. APPLICATION_EMAIL, [receiver_mail], reply_to=[settings.APPLICATION_EMAIL])
		email_msg.content_subtype = 'html'
		email_msg.send(fail_silently=False)

		tt.status = "Canceled"
		tt.save()
		return redirect('/orders/')

	else:
		return redirect('/orders/')

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""
def shoppingcart_view(request):
	global content
	t = request.user.id
	content = cart_1.objects.filter(uId=t)
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
		code = "E"
		t = Profile.objects.get(user_id=request.user.id)

		item = cart_1(pId=pId, qty=qty, pname=pname, uId=request.user.id, uo=t.oname, uname=request.user.username, code=code)
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
		t = Profile.objects.get(user_id=request.user.id)
		code = "V"

		item = cart_1(pId=pId, qty=qty, pname=pname, uId=request.user.id, uo=t.oname, uname=request.user.username, code=code)
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
		t1 = Profile.objects.get(user_id=request.user.id)
		code = "T"

		item = cart_1(pId=pId, qty=qty, pname=pname, uId=request.user.id, uo=t1.oname, uname=request.user.username, code=code)
		item.save()
		return render(request, "thread.html", {'threads':t, 'c':u})

	else:
		return render(request, "thread.html", {'threads':t, 'c':u})

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def log_out(request):
	
	global u
	u= "Null"
	auth.logout(request)
	return render(request, "view.html", {'c':u})

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def signin_view(request):

	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')

		user = auth.authenticate(username=email,password=password)

		if user is not None:
			global u
			auth.login(request, user)
			u = User.objects.get(username = request.user.username)

			p = Profile.objects.get(user_id = request.user.id)
			if p.address == "":
				return redirect("/register/")

			else:
				return redirect("/")

		else:
			messages.info(request,'INVALID CREDENTIALS')
			return render(request, "login.html", {})
			
	else:
		return render(request, "login.html", {})

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def checkout_view(request):
	e1 = elastic.objects.all()
	v1 = velcro.objects.all()
	t1 = thread.objects.all()
	l = Profile.objects.get(user_id=request.user.id)

	if l.address == "":
		return redirect("/register/")
		global m1
		m1 = "temp";
	else:
		return render(request, "checkout.html", {'c':u, 'profile':l, 'con':content, 'elastics_1':e1, 'velcros_1':v1, 'threads_1':t1})

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def order_1(request):
	if request.method == 'POST':
		global productamount
		
		productamount = request.POST.get('productamount')
		paymentmethod = request.POST.get('paymentmethod')
		status = request.POST.get('status')
		a = int(request.POST.get('productamount')) * 100
		
		e1 = elastic.objects.all()
		v1 = velcro.objects.all()
		t1 = thread.objects.all()
		t = Profile.objects.get(user_id=request.user.id)
		q1 = cart_1.objects.all().filter(uId = request.user.id)
		
		for x in q1:
			if paymentmethod == "Online Payment":
				keyid = 'rzp_test_u9Ub4CNVxWHXHL'
				keySecret = 'ZML84jcdmA6PF3202h74jEhk'
				client = razorpay.Client(auth=(keyid, keySecret))
				payment = client.order.create({'amount': a, 'currency':'INR', 'payment_capture': '1'})
				global a1
				m = order_6.objects.create(uid=request.user.id, uname=request.user.username, unumber=t.number, uorganisationname=t.oname, uemailaddress=request.user.email, uaddress=t.address, productname=x.pname, productid=x.pId, productcode=x.code, productqty=x.qty, productamount=productamount, paymentmethod=paymentmethod, status=status, payment_id=payment['id'], paid="True")
				a1=m.pk
				print (a)
				return render(request, "checkout.html", {'c':u, 'profile':t, 'con':content, 'elastics_1':e1, 'velcros_1':v1, 'threads_1':t1, 'payment':payment})
				
				q1.delete()

			else:
				m = order_6.objects.create(uid=request.user.id, uname=request.user.username, unumber=t.number, uorganisationname=t.oname, uemailaddress=request.user.email, uaddress=t.address, productname=x.pname, productid=x.pId, productcode=x.code, productqty=x.qty, productamount=productamount, paymentmethod=paymentmethod, status=status)
				a=m.pk
				tt = order_6.objects.get(id=a)				
				html_tpl_path = 'mail1.html'
				context_data = {'c':u, 'profile':t, 'con':tt}
				email_html_template = get_template(html_tpl_path).render(context_data)
				receiver_mail = request.user.email
				email_msg = EmailMessage('Order Placed', email_html_template, settings. APPLICATION_EMAIL, [receiver_mail], reply_to=[settings.APPLICATION_EMAIL])
				email_msg.content_subtype = 'html'
				email_msg.send(fail_silently=False)
								
				q1.delete()
				return redirect('/')

			

	else:
		return redirect('/checkout/')

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def order_view(request):
	o = order_6.objects.all()
	return render(request, "orders.html", {'c':u, 'con':o})

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def register(request):
	if request.method == 'POST':
		address = request.POST['address']
		oname = request.POST['oname']
		number = request.POST['number']

		t = Profile.objects.get(user_id=request.user.id)
		t.address = address
		t.oname = oname
		t.number = number
		t.save()

		if m1 == "Null":
			return redirect('/')
		else:
			return redirect('/checkout/')

	else:
		return render(request,"register.html", {'c':u})

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def psettings(request):
	return render(request, "settings.html", {'c':u})

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def changepassword(request):
	if request.method == 'POST':
		opassword = request.POST.get('opassword')
		npassword1 = request.POST.get('npassword1')
		npassword2 = request.POST.get('npassword2')

		if npassword1 == npassword2:
			u.set_password(npassword1)
			u.save()
			return redirect('/')
		else:
			messages.info(request,'Passwords Do Not Match')
			return redirect('/settings/')
	else:
		return render(request, "settings.html", {'c':u})

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def changeaddress(request):
	if request.method == 'POST':
		naddress = request.POST.get('naddress')

		t = Profile.objects.get(user_id=request.user.id)
		t.address = naddress
		t.save()
		return redirect('/')
	else:
		return render(request, "settings.html", {'c':u})

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def changenumber(request):
	if request.method == 'POST':
		newnumber = request.POST.get('nphone')

		t = Profile.objects.get(user_id=request.user.id)
		t.number = newnumber
		t.save()
		return redirect('/')
	else:
		return render(request, "settings.html", {'c':u})

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def panel(request):
	o = order_6.objects.all()
	return render(request, "panel.html", {'c':u, 'o':o})

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def confirmorder(request):

	if request.method == 'POST':
		cId = request.POST.get('cId')
		tt = order_6.objects.get(id=cId)

		tt.status = "Confirmed"
		tt.save()
		return redirect('/panel/')

	else:
		return redirect('/panel/')

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def outfordelivery(request):

	if request.method == 'POST':
		cId = request.POST.get('cId')
		tt = order_6.objects.get(id=cId)
		tt.status = "Out For Delivery"
		tt.save()
		return redirect('/panel/')

	else:
		return redirect('/panel/')

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def delivered(request):

	if request.method == 'POST':
		cId = request.POST.get('cId')
		tt = order_6.objects.get(id=cId)

		tt.status = "Delivered"
		tt.save()
		return redirect('/panel/')

	else:
		return redirect('/panel/')

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def addquantity(request):

	if request.method == 'POST':
		dId = request.POST.get('dId')
		tt = cart_1.objects.get(id=dId)
		t = int(tt.qty)
		tt.qty = t + 1
		tt.save()
		return redirect('/shoppingcart/')

	else:
		return redirect('/shoppingcart/')

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def delquantity(request):

	if request.method == 'POST':
		dId = request.POST.get('dId')
		tt = cart_1.objects.get(id=dId)
		t = int(tt.qty)
		tt.qty = t - 1
		tt.save()
		return redirect('/shoppingcart/')

	else:
		return redirect('/shoppingcart/')

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def changeorgname(request):
	if request.method == 'POST':
		neworgname = request.POST.get('norgname')

		t = Profile.objects.get(user_id=request.user.id)
		t.oname = neworgname
		t.save()
		return redirect('/')
	else:
		return render(request, "settings.html", {'c':u})


"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def success(request):
	if request.method == "POST":
		a = request.POST
		print(a)

		cId = request.POST.get('cId')
		tt = order_6.objects.get(id=a1)
		t = Profile.objects.get(user_id=request.user.id)

		html_tpl_path = 'mail1.html'
		context_data = {'c':u, 'profile':t, 'con':tt}
		email_html_template = get_template(html_tpl_path).render(context_data)
		receiver_mail = request.user.email
		email_msg = EmailMessage('Order Placed', email_html_template, settings. APPLICATION_EMAIL, [receiver_mail], reply_to=[settings.APPLICATION_EMAIL])
		email_msg.content_subtype = 'html'
		email_msg.send(fail_silently=False)


		return redirect('/')


"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

def paid(request):

	if request.method == 'POST':
		cId = request.POST.get('cId')
		tt = order_6.objects.get(id=cId)

		tt.paid = "True"
		tt.save()
		return redirect('/panel/')

	else:
		return redirect('/panel/')

"""--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------"""

