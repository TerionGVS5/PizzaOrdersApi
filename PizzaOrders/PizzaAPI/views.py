from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import AllowAny
from .models import OrderPizza
from .serializers import OrderPizzaSerializer


class OrderPizzaListCreateAPIView(ListCreateAPIView):
    queryset = OrderPizza.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = OrderPizzaSerializer
    lookup_field = 'uuid'


class OrderPizzaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = OrderPizza.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = OrderPizzaSerializer
    lookup_field = 'uuid'
