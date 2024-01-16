from django.db import models

# Create your models here.
class Bank(models.Model):
    Bankdate=models.DateField()
    Bankname=models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    AccountNumber=models.CharField(max_length=50)
    IFSCcode=models.CharField(max_length=50)
    Email=models.CharField(max_length=30)

