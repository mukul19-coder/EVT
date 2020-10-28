from django.db import connections
from django.db import models

# Create your models here.
class client(models.Model):
	email= models.CharField(max_length=100)
	password= models.CharField(max_length=100)

def __str__(self):
    return self.email
    return self.password

class cart_1(models.Model):
	pId = models.CharField(max_length=100)
	qty = models.CharField(max_length=100)
	pname = models.CharField(max_length=100)
	uId = models.CharField(max_length=100)
	uo = models.CharField(max_length=100)
	uname = models.CharField(max_length=100)
	code = models.CharField(max_length=50)

def __str__(self):
	return self.pId
	return self.qty
	return self.pname
	return self.uId
	return self.uo
	return self.uname
	return self.code

class order_6(models.Model):
	uid = models.CharField(max_length=100)
	uname = models.CharField(max_length=100)
	unumber = models.CharField(max_length=100)
	uorganisationname = models.CharField(max_length=100)
	uemailaddress = models.CharField(max_length=100)
	uaddress = models.CharField(max_length=100)
	productname = models.CharField(max_length=100)
	productid = models.CharField(max_length=100)
	productcode = models.CharField(max_length=100)
	productqty = models.CharField(max_length=100)
	productamount = models.CharField(max_length=100)
	payment = models.CharField(max_length=100)
	aname = models.CharField(max_length=100)
	anumber = models.CharField(max_length=100)
	bname = models.CharField(max_length=100)
	transactionid = models.CharField(max_length=100)
	status = models.CharField(max_length=100)

def __str__(self):
	return self.uid
	return self.uname
	return self.unumber
	return self.uorganisationname
	return self.uemailaddress
	return self.uaddress
	return self.productname
	return self.productid
	return self.productcode
	return self.productqty
	return self.productamount
	return self.payment
	return self.aname
	return self.anumber
	return self.bname
	return self.transactionid
	return self.status
