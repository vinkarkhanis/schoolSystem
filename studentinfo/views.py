from django.shortcuts import render
from .models import Student


def index(request):
    dests = Student.objects.all()

    return render(request, 'index.html', {'dests': dests})