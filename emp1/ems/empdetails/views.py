from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Employee

def employee_list(request):
    emp = Employee.objects.all()
    return HttpResponse(emp)