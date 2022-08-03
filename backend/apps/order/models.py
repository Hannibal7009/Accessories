from django import db
from django.db import models
from apps.users.models import User
from apps.products.models import Product

# Create your models here.


class Order(models.Model):
    class Meta(object):
        db_table = 'order'

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, db_index=True
    )

    total_price = models.FloatField(
        'Total Price', blank=False, null=False, db_index=True
    )

    customer_name = models.CharField(
        'Customer Name', max_length=255, blank=False, null=False, db_index=True
    )

    address = models.CharField(
        'Address', max_length=255, blank=False, null=False, db_index=True
    )

    building_type = models.CharField(
        'Building Type', max_length=255, blank=True, null=True, db_index=True
    )

    city = models.CharField(
        'City', max_length=255, blank=False, null=False, db_index=True
    )

    state = models.CharField(
        'State', max_length=255, blank=False, null=False, db_index=True
    )

    pin_code = models.CharField(
        'Pin Code', max_length=255, blank=False, null=False, db_index=True
    )

    total_qty = models.IntegerField(
        'Total Qty', max_length=11, blank=False, null=False, db_index=True
    )

    customer_phone = models.IntegerField(
        'Customer Phone', blank=True, null=True, db_index=True
    )

    created_at = models.DateTimeField(
        'Created At', blank=True, auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Updated At', blank=True, auto_now=True
    )


class OrderItem(models.Model):
    class Meta(object):
        db_table = 'order_item'

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, db_index=True
    )

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_index=True
    )

    quantity = models. IntegerField(
        'Quantity', blank=False, null=False, db_index=True
    )

    created_at = models.DateTimeField(
        'Created At', blank=True, auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Updated At', blank=True, auto_now=True
    )
