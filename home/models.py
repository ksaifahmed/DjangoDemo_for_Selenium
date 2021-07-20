from django.db import models
from home.forms import *


class Product(models.Model):
    name = models.CharField(max_length=250)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    discount = models.FloatField(default=0.0)
    location = models.CharField(choices=AREA_CHOICES, max_length=100)
    warranty = models.CharField(choices=YES_NO_CHOICES, max_length=20)

    # radio button
    refund = models.BooleanField(default=False)
    exchange = models.BooleanField(default=False)
    free_delivery = models.BooleanField(default=False)
    free_service = models.BooleanField(default=False)
