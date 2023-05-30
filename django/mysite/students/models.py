from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    age = models.IntegerField()
    active = models.CharField(max_length=10)
    level = models.CharField(max_length=10)
    dept = models.CharField(max_length=3)
    date = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=25)
    phone_Num = models.CharField(max_length=11)


class GraduatedStudent(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    dept = models.CharField(max_length=3)
