from django import forms

from .models import Participants

class RegistrationForm(forms.Form):
    email = forms.EmailField(label="Enter your email") 