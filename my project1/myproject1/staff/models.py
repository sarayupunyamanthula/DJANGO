

# Create your models here.
from django.db import models

class staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.CharField(max_length=100)

