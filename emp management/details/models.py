from django.db import models

# Create your models here
class employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)



    def __str__(self):
        return f"employee object ({self.id})"

