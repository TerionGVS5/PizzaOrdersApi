from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.OrderPizzaListCreateAPIView.as_view(), name='api_pizza_order'),
    url(r'^(?P<uuid>[-\w]+)/$', views.OrderPizzaRetrieveUpdateDestroyAPIView.as_view(), name='api_pizza_order'),
]