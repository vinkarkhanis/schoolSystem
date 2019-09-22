from django.shortcuts import render
from .models import Student
from tablib import Dataset
from .resources import StudentResource


def index(request):
    dests = Student.objects.all()

    return render(request, 'index.html', {'dests': dests})

