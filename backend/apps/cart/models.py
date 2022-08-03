from django import db
from django.db import models

# Create your models here.


class Cart(models.Model):
    class Meta(object):
        db_table = 'cart'

    quantity = models.IntegerField(
        'Quantity', blank=False, null=False, db_index=True
    )

    created_at = models.DateTimeField(
        'Created At', blank=True, auto_now_add=True
    )

    update_at = models.DateTimeField(
        'Update At', blank=True, auto_now=True
    )
