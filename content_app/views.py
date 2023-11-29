from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from .models import FAQ, Content, ContentType
from collections import defaultdict


# Create your views here.
def home(request):
    articles = Content.objects.filter(contentType=ContentType.article, isPremium=False).order_by('-publish')[:4]
    blogs = Content.objects.filter(contentType=ContentType.blog, isPremium=False).order_by('-publish')[:4]
    return render(request, 'home.html', {'articles': articles, 'blogs': blogs})


def faq_view(request):
    faqs = FAQ.objects.all()
    faq_by_category = defaultdict(list)
    for faq in faqs:
        faq_by_category[faq.category].append(faq)
    return render(request, 'FAQ.html', {'faq_by_category': dict(faq_by_category)})


def articles_view(request):
    if request.user.is_authenticated:
        articles = Content.objects.filter(contentType=ContentType.article).order_by('-publish')
    else:
        articles = Content.objects.filter(contentType=ContentType.article, isPremium=False).order_by('-publish')

    return render(request, 'articles.html', {'articles': articles})


def articles_search(request):
    query = request.GET.get('q', '')
    base_query = Content.objects.filter(title__icontains=query, contentType=ContentType.article)

    if request.user.is_authenticated:
        articles = base_query
    else:
        articles = base_query.filter(isPremium=False)

    return render(request, 'articles.html', {'articles': articles, 'query': query})


def articles_detail(request, slug):
    article = get_object_or_404(Content, slug=slug, contentType=ContentType.article)

    # Check if the article is premium and the user is not authenticated
    if article.isPremium and not request.user.is_authenticated:
        # redirect to login page
        return HttpResponseForbidden("This is premium content. Please login to access.")

    return render(request, 'article_detail.html', {'article': article})


def blog_view(request):
    if request.user.is_authenticated:
        blogs = Content.objects.filter(contentType=ContentType.blog).order_by('-publish')
    else:
        blogs = Content.objects.filter(contentType=ContentType.blog, isPremium=False).order_by('-publish')

    return render(request, 'blog.html', {'blogs': blogs})


def blog_detail(request, slug):
    blog = get_object_or_404(Content, slug=slug, contentType=ContentType.blog)

    # Check if the blog is premium and the user is not authenticated
    if blog.isPremium and not request.user.is_authenticated:
        # redirect to login page
        return HttpResponseForbidden("This is premium content. Please login to access.")

    return render(request, 'blog_detail.html', {'blog': blog})


def blog_search(request):
    query = request.GET.get('q', '')
    base_query = Content.objects.filter(title__icontains=query, contentType=ContentType.blog)

    if request.user.is_authenticated:
        blogs = base_query
    else:
        blogs = base_query.filter(isPremium=False)

    return render(request, 'blog.html', {'blogs': blogs, 'query': query})


def podcast_view(request):
    return render(request, 'podcast.html')
