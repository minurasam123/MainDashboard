from django.db import models

# Create your models here.
class Account(models.Model):
    account_types = (
        (1,"Lecturer"),
        (2,"Student"),
    )
    acc_type = models.IntegerField(choices=account_types,default=2)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    
    def __init__(self, *args, **kwargs):
        super(Account, self).__init__(acc_type,username,password)
    
class Lecturer(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    lec_NIC = models.CharField(max_length=10)
    first_Name = models.CharField(max_length=200, null=True)
    last_Name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)


class Student(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    lecturer = models.ForeignKey(Lecturer,on_delete=models.CASCADE, null=True)
    cima_ID = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=200, null=True)
    first_Name = models.CharField(max_length=200, null=True)
    last_Name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)

class Courses(models.Model):
    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=100)
    level = (
        (1,"Certificate level"),
        (2,"Operational Level"),
        (3,"Management Level"),
        (4,"Strategic Level"), 
        )
    course_level = models.IntegerField(choices=level)
    lecturer = models.ForeignKey(Lecturer,on_delete=models.CASCADE, null=True)
    student = models.ManyToManyField(Student)

class content(models.Model):
    content = (
        ("mp4","mp4"),
        ("pdf","pdf"),
        ("csv","csv")
    )
    cont_name = models.CharField(max_length=100)
    student = models.ManyToManyField(Student)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE,null=True)
    
class Exams(models.Model):
    exam_type = (
        (1,"mock exam"),
        (2,"Quiz"),
        (3,"Case Study"),
        )
    exam = models.IntegerField(choices=exam_type)


