from django.db import models
import uuid
from decimal import Decimal
from authenticate.models import CustomUser
from shortuuid.django_fields import ShortUUIDField
from django.core.validators import MinValueValidator

class Account(models.Model):
    ACCOUNT_TYPES = (
        ('SAV', 'Savings'),
        ('CHK', 'Checking'),
        ('MMA', 'Money Market'),
        ('CD', 'Certificate of Deposit'),
        ('IRA', 'Individual Retirement'),
    )
    
    CURRENCIES = (
        ('FCFA', 'Central Africa Franc'),
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('GBP', 'British Pound'),
    )
    
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('DORMANT', 'Dormant'),
        ('FROZEN', 'Frozen'),
        ('CLOSED', 'Closed'),
    )

    id= models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    account_id = ShortUUIDField(
        unique=True,
        length= 9,
        max_length=15,
        prefix= 'ACC',
        alphabet ='1234567890'
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    account_number = ShortUUIDField(
        unique=True,
        max_length=30,
        length=11,
        prefix='234',
        alphabet= '1234567890'
    )
    account_balance = models.DecimalField(
        decimal_places=2,
        max_digits=20, 
        default=0.00,
        validators=[MinValueValidator(Decimal('0.00'))]
        )
    account_type = models.CharField(max_length=5, choices=ACCOUNT_TYPES, default='SAV')
    currency = models.CharField(max_length=10, choices=CURRENCIES, default='FCFA')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE') 
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Bank Account'
        verbose_name_plural = 'Bank Accounts'    

    def __str__(self):
        name_parts = []
        if getattr(self.user, 'first_name', None):
            name_parts.append(self.user.first_name)
        if getattr(self.user, 'last_name', None):
            name_parts.append(self.user.last_name)
        
        user_display = ' '.join(name_parts) if name_parts else self.user.email
        return f"{self.account_number} - {user_display}"



    # class Profile(models.Model):
    #     user= models.OneToOneField(CustomUser, on_delete=None)

    
    # class Loan(models.Model):
    #     pass 