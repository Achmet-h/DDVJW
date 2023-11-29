from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.custom_logout, name='logout'),
    path('persoonlijke-gegevens/', views.update_profile, name='update_profile'),
    path('mijn-profiel/', views.profile_view, name='profile'),

]
