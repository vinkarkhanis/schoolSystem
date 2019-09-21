
from django.urls import path
from . import views

urlpatterns=[
    path('paymentsetup',views.paymentsetup,name='paymentsetup'),
]