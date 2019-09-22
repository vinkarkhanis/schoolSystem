from django.contrib import admin
from django.forms import forms

from .models import Student,Fees
from import_export.admin import ImportExportModelAdmin

admin.site.register(Student)
admin.site.register(Fees)

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    pass




    


