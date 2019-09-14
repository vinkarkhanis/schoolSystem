from django.db import models


# Create your models here.

class Student(models.Model):
    rollNum = models.IntegerField()
    name = models.TextField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    std = models.IntegerField()
    div = models.TextField()
    religion = models.TextField()
    cast = models.TextField()
    category = models.TextField()