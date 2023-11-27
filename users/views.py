from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import SignUpForm, LoginForm, ContactForm
from django.contrib import messages
from django.utils.translation import gettext as _


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # User activation can be done here if needed by an email sent to the user
            user.is_active = True
            user.save()
            login(request, user)
            messages.success(request, _('Uw account is aangemaakt'))
            return redirect('login')  # Redirect to a success page or home page
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Redirect to a success page or home page
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('home')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            telephone = form.cleaned_data['telephone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # assemble the message
            message = f'Bericht van {first_name} {last_name} {telephone} ({email}):\n{message}'

            # send the email
            send_mail(
                'Contactformulier DDVJW',
                message,
                email,
                ['hosting mailadres'], fail_silently=False,
            )
            return render(request, 'content_app/components/thankyou.html')
    else:
        form = ContactForm()
    return render(request, 'content_app/contact.html', {'form': form})
