from django.contrib import admin
from django.forms import forms

from .models import Student,Fees
from import_export.admin import ImportExportModelAdmin


admin.site.register(Fees)

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ('rollNum','student_class','surname','first_name','pending_fees')
    list_filter = ('category','religion','cast','total_fee_received',)
    search_fields = ('surname','first_name','rollNum',)
    fields = (
        'rollNum','first_name','middle_name','surname','gender','address','std','div','religion','cast','category','dob',
        'joining_date','leaving_date','birth_place','prev_school','student_id','aadhar_no','register_no'
    )

    def student_class(self,obj):
        return "{} {}".format(obj.std, obj.div)
    def pending_fees(self,obj):
        return obj.fees




    


