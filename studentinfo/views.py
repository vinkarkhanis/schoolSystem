from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datetime_safe import datetime
from django.views import View
from datetime import datetime

from studentinfo.utils import render_to_pdf

from payment.models import PaymentInfo
from .models import Student
from tablib import Dataset
from .resources import StudentResource


def index(request):
    dests = Student.objects.all()

    return render(request, 'index.html', {'dests': dests})

def GeneratePdf(request,object_id):
    # Retrieve data or whatever you need

    userName = "Sanket Bhumkar001"
    payment=PaymentInfo.objects.get(id=object_id)
    student=Student.objects.get(id=payment.rollNum.id)
    now = datetime.now()
    receiptNo = str(payment.receiptNo)
    date = now.strftime("%d/%m/%Y")
    day = now.strftime("%A")
    #onclick = "location.href='/pdf'"
    studentName = str(student.first_name)
    amount = payment.payment
    return render_to_pdf(
        'pdfTemplate.html',
        {
            'pagesize': 'A4',
            'studentName' : studentName,
            'amount' : amount,
            'date': date,
            'receiptNo': receiptNo,
            'day' : day
        }
    )

def request_page(request):
  if(request.GET.get('print')):
    return GeneratePdf(request)
