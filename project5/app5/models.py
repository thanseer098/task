from django.db import models

# Create your models here.
class Register (models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    place=models.CharField(max_length=25)
    photo=models.ImageField(upload_to='media/',null=True,blank=True)
    email=models.CharField(max_length=25)
    password=models.CharField(max_length=10)
class Gallary (models.Model):
    brand=models.CharField(max_length=25)
    name=models.CharField(max_length=25)
    photo=models.ImageField(upload_to='media/',null=True,blank=True)
    price=models.CharField(max_length=250)



    