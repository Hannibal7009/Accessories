from .models import Order
from rest_framework import serializers
from dataclasses import fields


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
