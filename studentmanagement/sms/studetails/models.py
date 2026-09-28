from django.db import models

# Create your models here.
class student(models.Model):
    s_name = models.CharField(max_length=100)   
    student_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    year_of_study = models.IntegerField()
    course = models.CharField(max_length=100)
    date_of_admission = models.DateField()
    active_inactivestatus = models.BooleanField(default=True)