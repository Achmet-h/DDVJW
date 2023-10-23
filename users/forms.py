from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'telephone', 'school_name', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
