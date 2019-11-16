from django.shortcuts import render
from django.http import HttpResponse
from .models import PaymentInfo
from studentinfo.models import Student


def paymentsetup(request):
    if request.method == 'POST':
        rollNumber = request.POST['rollNumber']
        standard = request.POST['standard']
        division = request.POST['division']
        student= Student.objects.get(rollNum=rollNumber,std=standard,div=division)
        print(student.name)

        payment_info=list(PaymentInfo.objects.filter(rollNum=student))
        for pay in payment_info:
            print(pay.dateTxn)

