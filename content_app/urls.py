from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import users.views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),

    # article views
    path('artikels/', views.articles_view, name='articles_view'),
    path('artikels/<slug:slug>/', views.articles_detail, name='article_detail'),
    path('zoek-artikel/', views.articles_search, name='article_search'),
    # blog View
    path('blog/', views.blog_view, name='blog_view'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('zoek-blog/', views.blog_search, name='blog_search'),
    # premium content views
    path('premium-artiekls/', views.premium_articles_view, name='premium_articles_view'),
    # FAQ view
    path('faq/', views.faq_view, name='FAQ'),

    # contact view
    path('contact/', users.views.contact_view, name='contact'),
]

# this is needed during the development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
