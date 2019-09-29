from django.contrib import admin
from django.forms import forms

from .models import Student,Fees
from import_export.admin import ImportExportModelAdmin


admin.site.register(Fees)

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ('rollNum','student_class','surname','first_name')
    list_filter = ('category','religion','cast',)
    search_fields = ('surname','first_name','rollNum',)
    fields = (
        'rollNum','first_name','surname','gender','address','std','div','religion','cast','category'
    )

    def student_class(self,obj):
        return "{} {}".format(obj.std, obj.div)




    


