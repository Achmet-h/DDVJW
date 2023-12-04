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
    # Define the order of categories
    category_order = [
        'Vragen over didactiek',  # Didactiek
        'Vragen over pedagogiek',  # Pedagogiek
        'Algemene vragen over lesgeven',  # Algemeen
        'Training en coaching'  # Begeleiding
    ]

    faq_by_category = {cat: [] for cat in category_order}  # Initialize with predefined order

    for faq in FAQ.objects.all():
        category_display = faq.get_category_display()
        if category_display in faq_by_category:
            faq_by_category[category_display].append(faq)

    # Ensure only categories with FAQs are passed to the template
    faq_by_category = {k: v for k, v in faq_by_category.items() if v}

    context = {'faq_by_category': faq_by_category}
    return render(request, 'FAQ.html', context)


def articles_view(request):
    if request.user.is_authenticated:
        articles = Content.objects.filter(contentType=ContentType.article).order_by('-publish')
    else:
        articles = Content.objects.filter(contentType=ContentType.article, isPremium=False).order_by('-publish')

    return render(request, 'articles.html', {'articles': articles})


def homepage_view(request):
    # Fetching articles
    if request.user.is_authenticated:
        latest_articles = Content.objects.filter(contentType=ContentType.article).order_by('-publish')[:4]
    else:
        latest_articles = Content.objects.filter(contentType=ContentType.article, isPremium=False).order_by('-publish')[
                          :4]

    # Fetching blogs
    if request.user.is_authenticated:
        latest_blogs = Content.objects.filter(contentType=ContentType.blog).order_by('-publish')[:4]
    else:
        latest_blogs = Content.objects.filter(contentType=ContentType.blog, isPremium=False).order_by('-publish')[:4]

    return render(request, 'home.html', {'articles': latest_articles, 'blogs': latest_blogs})


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
