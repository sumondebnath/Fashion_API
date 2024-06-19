from django.db import models
from django.contrib.auth.models import User
from category.models import Category
from product.constants import GENDER_TYPE, SIZE_TYPE

# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="product/images/", null=True, blank=True)
    product_number = models.IntegerField(unique=True)
    brand_number = models.CharField(max_length=30)
    size = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_type = models.CharField(max_length=255)
    gender_type = models.CharField(max_length=10, choices=GENDER_TYPE)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.price}"
