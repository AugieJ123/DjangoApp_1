from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *

# This class is for user to edit there account-info
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

# This class is for user to make an order
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

# This class is for user to create their own account
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']