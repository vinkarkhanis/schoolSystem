from random import randint

from django.db import models
from django.template.defaultfilters import slugify
from studentinfo.models import Student


# Create your models here.

class PaymentInfo(models.Model):
    rollNum = models.ForeignKey(Student, on_delete=models.CASCADE)
    payment = models.FloatField()
    dateTxn = models.DateField()
    class Meta:
        verbose_name_plural = 'Payment Information'
    # def __str__(self):
    #     return  "Payment: "+str(self.rollNum.rollNum)
