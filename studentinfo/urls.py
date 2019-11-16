from django.urls import path
from . import views

urlpatterns=[
    path('pdf',views.GeneratePdf,name='pdf'),
    path('print',views.request_page,name='print'),
]