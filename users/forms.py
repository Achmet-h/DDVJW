from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'telephone', 'school_name', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")


class ContactForm(forms.Form):
    first_name = forms.CharField(label='Voornaam', max_length=100)
    last_name = forms.CharField(label='Achternaam', max_length=100)
    telephone = forms.CharField(label='Telefoonnummer', max_length=15)
    email = forms.EmailField(label='Emailadres')
    message = forms.CharField(label='Vraag of opmerking', widget=forms.Textarea, max_length=500)
