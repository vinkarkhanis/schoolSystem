from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datetime_safe import datetime
from django.views import View
from datetime import datetime

from studentinfo.utils import render_to_pdf
from .models import Student
from tablib import Dataset
from .resources import StudentResource


def index(request):
    dests = Student.objects.all()

    return render(request, 'index.html', {'dests': dests})

def GeneratePdf(request):
    # Retrieve data or whatever you need
    userName = "Sanket Bhumkar001"
    now = datetime.now()
    receiptNo = now.strftime("%d%m%y%H%M")
    date = now.strftime("%d/%m/%Y")
    day = now.strftime("%A")
    studentName = Student.first_name
    amount = "2000"
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
