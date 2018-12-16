from rest_framework import serializers
from pizzaApp.mixins import UpdateSerializerMixin
from .models import OrderItems,Order
from .custom_fields import CustomerNameField,CustomerAddressField

class OrderItemsSerializer(UpdateSerializerMixin,serializers.ModelSerializer):
    customer_name = CustomerNameField(max_length=20)
    customer_address = CustomerAddressField(max_length=50)

    class Meta:
        model = OrderItems
        fields = (
            'id',
            'order',
            'customer_name',
            'customer_address',
            'pizza',
            'size',
            'quantity',
            'price'
        )
        read_only_fields = (
            'id',
            'order',
            'price'
        )

class OrderSerializer(UpdateSerializerMixin,serializers.ModelSerializer):
    items = OrderItemsSerializer(many=True)
    class Meta:
        model = Order
        fields = (
            'id',
            'status',
            'customer_name',
            'customer_address',
            'total',
            'items'
        )
        read_only_fields = (
            'id',
            'total',
            'items'
        )