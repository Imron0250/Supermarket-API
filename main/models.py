from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    status = models.IntegerField( choices=[
        (1, 'director'),
        (2, 'manager'),
        (3, 'call center'),
    ], default=3)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    cost = models.IntegerField()


class Client(models.Model):
    name = models.CharField(max_length=255)
    debt = models.IntegerField()

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField()
    quantity = models.CharField(max_length=255)

class Kassa(models.Model):
    sof_foyda = models.IntegerField()
    umumiy = models.IntegerField()
