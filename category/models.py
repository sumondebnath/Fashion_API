from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name