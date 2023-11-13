from django.shortcuts import render, get_object_or_404
from .models import FAQ, Content, ContentType
from collections import defaultdict
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'content_app/home.html')


def faq_view(request):
    faqs = FAQ.objects.all()
    faq_by_category = defaultdict(list)
    for faq in faqs:
        faq_by_category[faq.category].append(faq)
    return render(request, 'FAQ.html', {'faq_by_category': dict(faq_by_category)})


def articles_view(request):
    articles = Content.objects.filter(contentType=ContentType.article).order_by('-publish')
    return render(request, 'articles.html', {'articles': articles})


def articles_search(request):
    query = request.GET.get('q', '')
    if query:
        articles = Content.objects.filter(
            title__icontains=query,
            contentType=ContentType.article
        )
    else:
        # If no query, return all articles
        articles = Content.objects.filter(contentType=ContentType.article)

    return render(request, 'articles.html', {'articles': articles, 'query': query})


def articles_detail(request, slug):
    article = get_object_or_404(Content, slug=slug)
    return render(request, 'article_detail.html', {'article': article})


def blog_view(request):
    blogs = Content.objects.filter(contentType=ContentType.blog).order_by('-publish')
    return render(request, 'blog.html', {'blogs': blogs})


def blog_detail(request, slug):
    blog = get_object_or_404(Content, slug=slug, contentType=ContentType.blog)
    return render(request, 'blog_detail.html', {'blog': blog})


def blog_search(request):
    query = request.GET.get('q', '')
    if query:
        blogs = Content.objects.filter(
            title__icontains=query,
            contentType=ContentType.blog
        )
    else:
        blogs = Content.objects.filter(contentType=ContentType.blog)

    return render(request, 'blog.html', {'blogs': blogs, 'query': query})


@login_required
def premium_articles_view(request):
    premium_contents = Content.objects.filter(isPremium=True, ContentType='article')
    return render(request, 'premium_articles.html', {'premium_contents': premium_contents})


