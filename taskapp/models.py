from django.db import models


class Signup(models.Model):
    username=models.CharField(max_length=100,blank=False,null=False)
    email=models.EmailField(max_length=40,blank=False,unique=True,null=False)
    address=models.CharField(max_length=100,blank=False,null=False)
    password=models.CharField(max_length=15,blank=False,null=False)
   


# Create your models here.
