from django.shortcuts import render

# Create your views here.
from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_duration = models.CharField(max_length=50)
    course_fee = models.DecimalField(max_digits=10, decimal_places=2)
    trainer_name = models.CharField(max_length=100)
    mode = models.CharField(max_length=20)
    start_date = models.DateField()
    number_of_seats = models.IntegerField()
    course_active = models.BooleanField(default=True)

