from django.db import connections
from django.db import models

# Create your models here.
class client(models.Model):
	email= models.CharField(max_length=100)
	password= models.CharField(max_length=100)

def __str__(self):
    return self.email
    return self.password