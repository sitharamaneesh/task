
from django import forms
from django.forms.fields import EmailField
from .models import Signup
from django.forms import ModelForm
from django.forms import ValidationError

from taskapp import models

class SignupForm(forms.ModelForm):
    confirm=forms.CharField(max_length=30)
    email = forms.EmailField(
        widget = forms.TextInput(attrs = {'placeholder': 'email'}),
        required = True)
    class Meta:
        model=Signup
        fields="__all__"

class LoginForm(forms.ModelForm):
    
    class Meta:
        model=Signup
        exclude=['username','address']

class EditForm(forms.ModelForm):
    class Meta:
        model=Signup
        exclude=['password','email']
    