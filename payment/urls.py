
from django.urls import path
from . import views

app_name = "payment"
urlpatterns=[
    path('paymentsetup',views.paymentsetup,name='paymentsetup'),

]