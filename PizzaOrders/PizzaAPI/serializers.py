from rest_framework import serializers
from .models import OrderPizza


class OrderPizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPizza
        fields = ['pizza_size', 'customer_name', 'customer_address', 'uuid']
