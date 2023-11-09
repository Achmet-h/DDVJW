from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'content_app/home.html')


def FAQ(request):
    return render(request, 'content_app/FAQ.html')




