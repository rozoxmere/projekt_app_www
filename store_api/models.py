from django.conf import settings
from django.db import models
from datetime import datetime    

# Create your models here.


SIZE_CHOICES = [
    ("XS", "Extra Small"),
    ("S", "Small"),
    ("M", "Medium"),
    ("L", "Large"),
    ("XL", "Extra Large"),
]


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"



class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    price = models.FloatField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    size = models.CharField(choices=SIZE_CHOICES,
                            max_length=2, null=False, blank=False)
    amount = models.IntegerField(null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} {self.size}"


class OrderProductSize(models.Model):
    product_size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    amount_in_order = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.product_size} ({self.amount_in_order} szt)"

class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    # products = models.ManyToManyField(ProductSize)
    products = models.ManyToManyField(OrderProductSize, null=False, blank=False)
    order_date = models.DateTimeField(default=datetime.now)

    class Meta:
        get_latest_by = ["order_date"]
# reviews może
