from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from .forms import SignUpForm, LoginForm


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # User activation can be done here if needed by an email sent to the user
            user.is_active = True
            user.save()
            login(request, user)
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


def test_view(request):
    return render(request, "test.html")


def custom_logout(request):
    logout(request)
    return redirect('home')
