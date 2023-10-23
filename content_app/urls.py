from django.urls import path

import content_app.views
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),

]
