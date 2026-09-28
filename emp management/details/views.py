from django.http import HttpResponse
from .models import employee

def index(request):
    return HttpResponse("This is Index Page")

def employee_list(request):
    emp = employee.objects.all()
    return HttpResponse(emp)