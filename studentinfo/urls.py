from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('pdf',views.GeneratePdf,name='pdf'),
    path('print',views.request_page,name='print'),
]