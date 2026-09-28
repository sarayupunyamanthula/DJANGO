from django.http import HttpResponse
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return HttpResponse(courses)