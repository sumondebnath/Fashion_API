from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from review.constants import RATING

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    rating = models.CharField(max_length=10, choices=RATING, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.email