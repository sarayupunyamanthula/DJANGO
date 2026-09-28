from django.http import HttpResponse
from .models import department

def department_list(request):
    dept = department.objects.all()
    return HttpResponse(dept)