from django.urls import path

import content_app.views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),

]
