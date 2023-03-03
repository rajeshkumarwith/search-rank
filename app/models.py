from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.CharField(max_length=100)

class Contact(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    mobile=models.CharField(max_length=100,blank=True,null=True)