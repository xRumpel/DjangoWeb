from django import forms
from .models import User
from .models import Order

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'products']