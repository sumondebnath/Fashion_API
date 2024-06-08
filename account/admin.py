from django.contrib import admin
from account.models import UserAccount, UserAddress

# Register your models here.

admin.site.register(UserAddress)
admin.site.register(UserAccount)