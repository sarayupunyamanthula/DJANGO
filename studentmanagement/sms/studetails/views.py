from django.http import HttpResponse

from django.shortcuts import render
from .models import student
# Create your views here.
def student_list(request):
    students = student.objects.all()
    return HttpResponse(students)