from django.urls import path
from . import views #the dot means the current directory

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]