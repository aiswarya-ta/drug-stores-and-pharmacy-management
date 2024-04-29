from django.db import models

# Create your models here.
class inpatient_tbl(models.Model):
    name=models.CharField(max_length=25)
    num=models.IntegerField()
    email=models.EmailField()
    password=models.TextField(max_length=30)
    def __str__(self):
        return self.name

class outpatient_tbl(models.Model):
    name=models.CharField(max_length=25)
    num=models.IntegerField()
    email=models.EmailField()
    password=models.TextField(max_length=30)
    def __str__(self):
        return self.name

class inproducts_tbl(models.Model):
    img=models.FileField(upload_to='pic')
    title=models.CharField(max_length=100)
    des=models.TextField(max_length=300)
    price=models.IntegerField()
    def __str__(self):
        return self.title

class outproducts_tbl(models.Model):
    img=models.FileField(upload_to='pic')
    title=models.CharField(max_length=25)
    des=models.TextField(max_length=100)
    price=models.IntegerField()
    def __str__(self):
        return self.title
class inpayment_tbl(models.Model):
    name=models.CharField(max_length=40)
    address=models.CharField(max_length=300)
    numb=models.IntegerField()
    item=models.CharField(max_length=30)
    price=models.IntegerField()
    def __str__(self):
        return self.name

class outpayment_tbl(models.Model):
    name=models.CharField(max_length=40)
    address=models.CharField(max_length=300)
    numb=models.IntegerField()
    item=models.CharField(max_length=30)
    price=models.IntegerField()
    def __str__(self):
        return self.name


class out_order_tbl(models.Model):
    name=models.CharField(max_length=40)
    item=models.CharField(max_length=40)
    price=models.IntegerField()
    adress=models.CharField(max_length=40)
    def __str__(self):
        return self.name

    