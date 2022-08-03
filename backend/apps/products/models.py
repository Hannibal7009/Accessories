from email.mime import image
from django import db
from django.db import models
from config.constants import STATUS

# Create your models here.


class Product(models.Model):
    class Meta(object):
        db_table = 'product'

    status = models.CharField(
        'Status', max_length=50, blank=False, null=False, db_index=True, choices=STATUS
    )

    name = models.CharField(
        'Name', max_length=50, blank=False, null=False, db_index=True
    )

    description = models.CharField(
        "Description", max_length=50, blank=False, null=False, db_index=True
    )

    price = models.FloatField(
        'Price', blank=False, null=False, db_index=True
    )

    image = models.ImageField(
        'Image', blank=False, null=False, db_index=True
    )

    created_at = models.DateTimeField(
        'Created At', blank=True, auto_now_add=True
    )

    update_at = models.DateTimeField(
        'Update At', blank=True, auto_now=True
    )


def __str__(self):
    return self.name
