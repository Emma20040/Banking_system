from django.db import models
import uuid
from authenticate.models import CustomUser
from shortuuid.django_fields import ShortUUIDField

class Account(models.Model):
    id= models.UUIDField(
        primary_key=True,
        unique=True,
         default=uuid.uuid4,
         editable=False
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    account_balance = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    account_number = ShortUUIDField(
        unique=True,
        max_length=30,
        length=11,
        prefix='234',
        alphabet= '1234567890'
    )
    account_id = ShortUUIDField(
        unique=True,
        length= 9,
        max_length=15,
        prefix= 'ACC',
        alphabet ='1234567890'
    )
    date = models.DateTimeField(auto_now_add=True)
    