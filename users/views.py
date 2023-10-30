from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Make the user active for this example; consider sending email confirmation in real-world scenarios.
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('some_view_name')  # Redirect to a success page or home page
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('some_view_name')  # Redirect to a success page or home page
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def test_view(request):
    return render(request, "test.html")