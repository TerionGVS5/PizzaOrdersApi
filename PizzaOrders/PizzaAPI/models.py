from django.db import models
import uuid as uuid_lib


# Create your models here.
class OrderPizza(models.Model):
    size_30cm = '30cm'
    size_50cm = '50cm'
    sizes = (
        (size_30cm, '30cm'),
        (size_50cm, '50cm'),
    )
    pizza_size = models.CharField(
        max_length=4,
        choices=sizes,
        default=size_30cm,
    )
    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=300)
    uuid = models.UUIDField(  # Used by the API to look up the record
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)
