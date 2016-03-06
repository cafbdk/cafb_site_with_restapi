from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
    gtin_code = models.IntegerField()
    gtin_name = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
