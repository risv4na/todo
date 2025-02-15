from django.db import models

# Create your models here.


class ProductDetails(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=50)
    price = models.FloatField()
    stock_quantity = models.IntegerField()
    description = models.CharField(max_length=500)
