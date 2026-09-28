from django.shortcuts import render
from django.http import HttpResponse

from .models import student
def index(request):
    return HttpResponse("Hello world")

def home(request):
    return HttpResponse("Welcome to Home Page")

def products(request):
    return HttpResponse("This is Products Page")

def search(request):
    return HttpResponse("This is Search Page")

def recommendations(request):
    return HttpResponse("This is Recommendations Page")

def about(request):
    return HttpResponse("This is About Page")

def students(request):
    s = student.objects.all()
    return HttpResponse(s)
