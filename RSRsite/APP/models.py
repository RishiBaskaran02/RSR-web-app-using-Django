from django.db import models

# Create your models here.
class signin(models.Model):
      fullname = models.CharField(max_length=100)
      email = models.CharField(max_length=100)
      DOB = models.DateField()
      Phone = models.IntegerField()
      password = models.CharField(max_length=100)
      address = models.CharField(max_length=100, default='default: India, You can update this field in edit Profile')

class OfficeSignin(models.Model):
      username = models.CharField(max_length=100)
      email = models.CharField(max_length=100)
      DOB = models.DateField()
      Phone = models.IntegerField()
      password = models.CharField(max_length=100)

class Adminsignin(models.Model):
      Username = models.CharField(max_length=100)
      email = models.CharField(max_length=100)
      DOB = models.DateField()
      Phone = models.IntegerField()
      password = models.CharField(max_length=100)

class Verification(models.Model):
      fullname = models.CharField(max_length=100)
      email = models.CharField(max_length=100)
      phone = models.CharField(max_length=100)
      farmAddress = models.CharField(max_length=100)
      farmRegNo = models.IntegerField()
      certificate = models.FileField()
      verified = models.IntegerField(default=0)

class Product(models.Model):
      pname = models.CharField(max_length=100)
      pquantity = models.CharField(max_length=100)
     
def __unicode__(self):
      return self.name