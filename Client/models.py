from django.db import models

class client(models.Model):
	fname= models.CharField(max_length=100)
	lname= models.CharField(max_length=100)
	oname= models.CharField(max_length=100)
	number= models.CharField(max_length=100)
	address= models.CharField(max_length=100)
	email= models.CharField(max_length=100)
	password= models.CharField(max_length=100)

def __str__(self):
    return self.fname
    return self.lname
    return self.oname
    return self.number
    return self.address
    return self.email
    return self.password	
		