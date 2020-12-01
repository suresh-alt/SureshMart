from django.db import models

# Create your models here.
class Customer(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    username=models.CharField(max_length=30)
    password=models.IntegerField()


class productmodel(models.Model):
    pno=models.IntegerField()
    pname=models.CharField(max_length=30)
    price=models.IntegerField()
    quantity=models.IntegerField()
    pimage=models.ImageField(upload_to='suresh/')