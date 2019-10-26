from django.db import models
from studentinfo.models import Student


# Create your models here.

class PaymentInfo(models.Model):
    rollNum = models.ForeignKey(Student, on_delete=models.CASCADE)
    payment = models.FloatField()
    dateTxn = models.DateField()
    receipt = models.FileField(upload_to='receipts/', null=True, blank=True)
    # def __str__(self):
    #     return  "Payment: "+str(self.rollNum.rollNum)



