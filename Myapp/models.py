from django.db import models

# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    Birth_date = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    education = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
