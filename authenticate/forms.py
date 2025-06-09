from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields =['email', 'phone_number', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    email = forms.EmailField(label='Email')