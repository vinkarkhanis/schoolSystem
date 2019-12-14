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
from fiscalyear import FiscalYear
import fiscalyear

def GeneratePdf(request,object_id):
    # Retrieve data or whatever you need
    payment=PaymentInfo.objects.get(id=object_id)
    student=Student.objects.get(id=payment.rollNum.id)
    now = datetime.now()
    # receipt_no = str(payment.id)
    receipt_no = payment.receipt_no
    date = now.strftime("%d/%m/%Y")
    receipt_date = payment.dateTxn
    day = now.strftime("%A")
    roll_num = student.rollNum
    class_div = str(str(student.std) + " " + student.div)
    student_name = str(student.last_name + " " + student.first_name + " " + student.middle_name)
    gender = student.gender
    amount = payment.payment
    return render_to_pdf(
        'pdfTemplate.html',
        {
            'pagesize': 'A4',
            'studentName' : student_name,
            'amount' : amount,
            'date': date,
            'receiptNo': receipt_no,
            'day' : day,
            'rollNum' : roll_num,
            'class' : class_div,
            'receiptDate': receipt_date,
            'gender' : gender
        }
    )

def request_page(request):
  if(request.GET.get('print')):
    return GeneratePdf(request)

def generate_bonafide(request,object_id):
    # Retrieve data or whatever you need
    student=Student.objects.get(id=object_id)
    now = datetime.now()
    student_gen_reg_no = str(student.register_no)
    date = now.strftime("%d/%m/%Y")
    religion = student.religion
    caste=student.cast
    day = now.strftime("%A")
    class_div = str(str(student.std) + " " + student.div)
    birthplace=student.birth_place
    student_name = str(student.last_name + " " + student.first_name + " " + student.middle_name)
    dob=student.dob
    dob_string = dob.strftime('%A %d %B %Y')
    current_fiscal_year = FiscalYear.current()
    fiscalyear.setup_fiscal_calendar(start_month=6)
    fiscal_year = str(current_fiscal_year.start.year) + "-" + str(current_fiscal_year.end.year)
    gender = student.gender
    return render_to_pdf(
        'bonafide_certificate.html',
        {
            'pagesize': 'A4',
            'studentName' : student_name,
            'date': date,
            'religion': religion,
            'caste' : caste,
            'day' : day,
            'student_gen_reg_no' : student_gen_reg_no,
            'class' : class_div,
            'birthplace':birthplace,
            'dob':dob,
            'fiscal_year' : fiscal_year,
            'dob_string' : dob_string,
            'gender' : gender
        }
    )
