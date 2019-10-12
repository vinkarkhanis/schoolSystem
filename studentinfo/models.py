from django.db import models

from .reader import Reader


class Fees(models.Model):
    std = models.IntegerField()
    fees = models.FloatField()
    def __str__(self):
        return  "Std: "+str(self.std) + ' = ' + "₹"+str(self.fees)+"/-"

    class Meta:
        verbose_name_plural = "Fees"

class Student(models.Model):
    rollNum = models.IntegerField()
    first_name = models.CharField(max_length=101)
    middle_name = models.CharField(max_length=100,blank=True)
    surname=models.CharField(max_length=100)
    gender = models.CharField(choices=Reader.read('gender'),default=Reader.read('gender')[0],max_length=10)
    address = models.TextField()
    std = models.IntegerField(choices=Reader.read('standard','numeric'), default=Reader.read('standard','numeric')[0])
    div = models.TextField(choices=Reader.read('divison'), default=Reader.read('divison')[0])
    religion = models.CharField(max_length=50)
    cast = models.CharField(max_length=50)
    category = models.TextField(choices=Reader.read('categories'), default=Reader.read('categories')[0])
    fees=models.FloatField(blank=True, null=True)

    class Meta:
        unique_together = ('rollNum', 'div','std')

    def __str__(self):
        return  "Name - "+self.first_name+" --> "+"Class - "+str(self.std)+":"+self.div



