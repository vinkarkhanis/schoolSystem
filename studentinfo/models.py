from django.db import models




class Fees(models.Model):
    std = models.IntegerField()
    fees = models.FloatField()

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
    fees=models.FloatField()

