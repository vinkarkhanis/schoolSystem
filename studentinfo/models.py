from django.db import models

from . import ConfigReader


class Fees(models.Model):
    std = models.IntegerField()
    fees = models.FloatField()
    def __str__(self):
        return  "Std: "+str(self.std) + ' = ' + "₹"+str(self.fees)+"/-"

    class Meta:
        verbose_name_plural = "Fees"

class Student(models.Model):
    rollNum = models.IntegerField()
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100,blank=True)
    surname=models.CharField(max_length=100)
    gender = models.CharField(choices=ConfigReader.gender_reader(),default=ConfigReader.gender_reader()[0],max_length=10)
    address = models.TextField()
    std = models.IntegerField(choices=ConfigReader.standard_reader(), default=ConfigReader.standard_reader()[0])
    div = models.TextField(choices=ConfigReader.division_reader(), default=ConfigReader.division_reader()[0])
    religion = models.CharField(max_length=50)
    cast = models.CharField(max_length=50)
    category = models.TextField(choices=ConfigReader.category_reader(), default=ConfigReader.category_reader()[0])
    fees=models.FloatField(blank=True, null=True)

    class Meta:
        unique_together = ('rollNum', 'div','std')

    def __str__(self):
        return  "Name - "+self.first_name+" --> "+"Class - "+str(self.std)+":"+self.div



