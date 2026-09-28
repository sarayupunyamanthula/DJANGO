from django.contrib import admin
from django.urls import path
from myapp1 import views

urlpatterns = [
    
    path("index/",views.index),

    path("home/", views.home),
    path("products/", views.products),
    path("search/", views.search),
    path("recommendations/", views.recommendations),
    path("about/", views.about),    
    path("students/", views.students),
]