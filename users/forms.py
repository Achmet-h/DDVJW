import re
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='id_first_name', max_length=100, required=True)
    last_name = forms.CharField(label='id_last_name', max_length=100, required=True)
    email = forms.EmailField(label=_("id_email"), required=True)
    telephone = forms.CharField(label=_("id_telephone"), max_length=20, required=False)
    school_name = forms.CharField(label=_("id_school name"), max_length=100, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'telephone', 'school_name', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Dit emailadres bestaat al of is niet geldig")
        return email

    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        r = User.objects.filter(telephone=telephone)
        if r.count():
            raise ValidationError("Telefoonnummer is verplicht")
        return telephone

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        errors = []

        # Custom Validation for Password Length
        if len(password1) < 8:
            errors.append(_("Het wachtwoord is te kort. Het moet ten minste 8 karakters bevatten."))

        # Custom Validation for Numeric Passwords
        if password1.isdigit():
            errors.append(_("Het wachtwoord mag niet volledig numeriek zijn."))

        # Custom Validation for Common Passwords
        common_passwords = ['password', '12345678', 'qwerty', 'abc123']
        if password1.lower() in common_passwords:
            errors.append(_("Het wachtwoord is te gewoon."))

        # Custom Validation for Alphabetical Characters
        if not re.search('[a-zA-Z]', password1):
            errors.append(_("Het wachtwoord moet ten minste één letter bevatten."))

        # Custom Validation for Digits
        if not re.search('[0-9]', password1):
            errors.append(_("Het wachtwoord moet ten minste één cijfer bevatten."))

        # Custom Validation for Upper and Lower Characters
        if not re.search('[A-Z]', password1) or not re.search('[a-z]', password1):
            errors.append(_("Het wachtwoord moet een mix van hoofdletters en kleine letters bevatten."))

        # Custom Validation for Special Characters
        if not re.search('[!@#$%^&*(),.?":{}|<>]', password1):
            errors.append(_("Het wachtwoord moet ten minste één speciaal teken bevatten."))

        # Raise all validation errors
        if errors:
            raise ValidationError(errors)

        return password1


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise ValidationError(_("Emailadres of wachtwoord is onjuist"))
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class ContactForm(forms.Form):
    first_name = forms.CharField(label='Voornaam', max_length=100)
    last_name = forms.CharField(label='Achternaam', max_length=100)
    telephone = forms.CharField(label='Telefoonnummer', max_length=15)
    email = forms.EmailField(label='Emailadres')
    message = forms.CharField(label='Vraag of opmerking', widget=forms.Textarea, max_length=500)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'telephone', 'school_name']