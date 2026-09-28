from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import staff

def staff_list(request):
    st = staff.objects.all()
    return HttpResponse(st)