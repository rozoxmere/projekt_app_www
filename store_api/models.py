from django.conf import settings
from django.db import models

# Create your models here.


SIZE_CHOICES = [
    ("XS", "Extra Small"),
    ("S", "Small"),
    ("M", "Medium"),
    ("L", "Large"),
    ("XL", "Extra Large"),
]


class Category(models.Model):
    name = models.CharField(max_length=100, null=False)


class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    price = models.FloatField(null=False)
    category = models.ForeignKey(Category)


class ProductSize(models.Model):
    size = models.CharField(choices=SIZE_CHOICES, null=False, blank=False)
    amount = models.IntegerField(null=False, blank=False)
    product = models.ManyToOneRel(Product, on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    ))
    products = models.ManyToManyRel(ProductSize)
    # sprawdzic czy potrzebne w ogole
    total_amount = models.FloatField()



#reviews może