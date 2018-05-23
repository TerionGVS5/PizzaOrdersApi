import pytest
from django.test import Client
from .models import OrderPizza

pytestmark = pytest.mark.django_db


class TestOrderPizzaModel:

    def test_get_saved(self):
        c = Client()
        new_order_pizza = OrderPizza.objects.create(
            pizza_size="30cm",
            customer_name="Jonn",
            customer_address="Vladivostok"

        )
        response = c.get('/api/{}/'.format(new_order_pizza.uuid))
        assert response.status_code == 200

        assert response.json()['customer_name'] == "Jonn"

    def test_delete(self):
        c = Client()
        new_order_pizza = OrderPizza.objects.create(
            pizza_size="30cm",
            customer_name="Jonn",
            customer_address="Vladivostok"

        )
        response = c.delete('/api/{}/'.format(new_order_pizza.uuid))
        assert OrderPizza.objects.all().count() == 0
