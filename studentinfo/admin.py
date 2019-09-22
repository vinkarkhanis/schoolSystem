from django.contrib import admin
from django.forms import forms

from .models import Student,Fees
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

admin.site.register(Student)
admin.site.register(Fees)


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

# @admin.register(Student)
# class student_admin(admin.ModelAdmin, ExportCsvMixin):
    


