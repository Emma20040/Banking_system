from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator, MinLengthValidator
from django.utils.translation import gettext_lazy as _


# class singup custom users
class CustomUser(AbstractUser):
    username = None 

    email = models.EmailField(
        _('email address'),
        max_length=200,
        unique=True, 
        blank=False, 
        null=False,
        validators=[EmailValidator(message=_("Enter a valid email address"))],
        help_text=_('Required. Your active email address')
        )
    first_name= models.CharField(max_length=100, unique=False)
    last_name = models.CharField(max_length=100, unique=False)
    phone_number = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        validators=[MinLengthValidator(10)],
        help_text=_('Required. Your active phone number')
    )

    date_of_birth = models.DateField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = []  # No additional fields required for createsuperuser
    
    class Meta:
        verbose_name = _('Bank Customer')
        verbose_name_plural = _('Bank Customers')

    def __str__(self):
        return self.email