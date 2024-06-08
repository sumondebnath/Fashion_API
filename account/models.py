from django.db import models
from django.contrib.auth.models import User
from account.constants import GENDER_TYPE, ACCOUNT_TYPE

# Create your models here.

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    image = models.ImageField(upload_to="account/images/", null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE, null=True, blank=True)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=120, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}"