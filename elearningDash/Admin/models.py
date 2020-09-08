from django.db import models

# Create your models here.
class Student(models.Model):
    cima_ID = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=200, null=True)
    NIC = models.IntegerField(null=True)
    first_Name = models.CharField(max_length=200, null=True)
    last_Name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)

class Course(models.Model):
    