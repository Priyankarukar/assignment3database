from django.db import models

# Create your models here.
class Students(models.Model):
    uname=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Pnumber= models.CharField(max_length=50)
    Address = models.CharField(max_length=50)