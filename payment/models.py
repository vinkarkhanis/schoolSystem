
from random import randint

from django.db import models
from django.template.defaultfilters import slugify
from studentinfo.models import Student


# Create your models here.

class PaymentInfo(models.Model):
    rollNum = models.ForeignKey(Student, on_delete=models.CASCADE)
    payment = models.FloatField()
    dateTxn = models.DateField()
    receipt = models.FileField(upload_to='receipts/', null=True, blank=True)
    receiptNo = models.CharField(max_length=12,blank=True, unique=True, default=str('rcpt-'+str(randint(1,10))+str(randint(756, 9000))))
    # def __str__(self):
    #     return  "Payment: "+str(self.rollNum.rollNum)




