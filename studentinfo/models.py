import datetime

from django.db import models

from .reader import Reader


class Fees(models.Model):
    std = models.CharField(max_length=10,choices=Reader.read('standard'), default=Reader.read('standard')[0][0])
    fees = models.FloatField()
    def __str__(self):
        return  "Std: "+str(self.std) + ' = ' + "₹"+str(self.fees)+"/-"

    class Meta:
        verbose_name_plural = "Fees"

class Student(models.Model):
    rollNum = models.IntegerField()
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100,blank=True)
    last_name=models.CharField(max_length=100)
    gender = models.CharField(choices=Reader.read('gender'),default=Reader.read('gender')[0][0],max_length=10)
    address = models.TextField()
    std = models.CharField(max_length=10,choices=Reader.read('standard'), default=Reader.read('standard')[0][0])
    div = models.TextField(choices=Reader.read('divison'), default=Reader.read('divison')[0][0])
    religion = models.CharField(max_length=50)
    cast = models.CharField(max_length=50)
    category = models.TextField(choices=Reader.read('categories'), default=Reader.read('categories')[0][0])
    fees=models.FloatField(blank=True, null=True)
    dob = models.DateField()
    joining_date = models.DateField(blank=True,)
    leaving_date = models.DateField(blank=True,null=True)
    birth_place = models.CharField(max_length=100,)
    prev_school = models.TextField(blank=True,null=True)
    student_id = models.IntegerField()
    aadhar_no = models.CharField(max_length=20,blank=True)
    register_no = models.CharField(max_length=50,)
    total_fee_received = models.BooleanField(default=False)

    class Meta:
        unique_together = ('rollNum', 'div','std')

    def __str__(self):
        return  "Name - "+self.first_name+" --> "+"Class - "+str(self.std)+":"+self.div



