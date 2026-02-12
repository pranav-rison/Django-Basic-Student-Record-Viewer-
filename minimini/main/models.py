# mini
# mini121

from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)   
    grade=models.CharField(max_length=1)
    department=models.CharField(max_length=15)