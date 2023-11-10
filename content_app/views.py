from django.shortcuts import render
from .models import FAQ
from collections import defaultdict


# Create your views here.

def home(request):
    return render(request, 'content_app/home.html')


def faq_view(request):
    faqs = FAQ.objects.all()
    faq_by_category = defaultdict(list)
    for faq in faqs:
        faq_by_category[faq.category].append(faq)
    return render(request, 'FAQ.html', {'faq_by_category': dict(faq_by_category)})



