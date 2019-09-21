from django.shortcuts import render
from django.http import HttpResponse


def paymentsetup(request):
    return render(request, 'paymetSetup.html')
