from django.contrib.auth.forms import UserCreationForm
from app.models import User
from django import forms


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email', 'first_name', 'last_name', 'address', 'city', 'state', 'pin_code', 'password1', 'password2',]


class UserSignupEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['username', 'email', 'first_name', 'last_name', 'address', 'city', 'state', 'pin_code',]