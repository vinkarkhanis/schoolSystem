from django.conf.urls import url
from django.contrib import admin
from django.forms import forms
from django.urls import reverse
from django.utils.html import format_html

from .views import generate_bonafide
from .models import Student,Fees
from import_export.admin import ImportExportModelAdmin


admin.site.register(Fees)

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ('rollNum','student_class','last_name','first_name','pending_fees','print_bonafide')
    list_filter = ('category','religion','div','total_fee_received',)
    search_fields = ('last_name','first_name','rollNum',)
    fields = (
        'rollNum','first_name','middle_name','last_name','gender','address','std','div','religion','cast','category','dob',
        'joining_date','leaving_date','birth_place','prev_school','student_id','aadhar_no','register_no','student_active',
        'exempt_fee'
    )

    def student_class(self,obj):
        return "{} {}".format(obj.std, obj.div)
    def pending_fees(self,obj):
        return obj.fees

    def print_bonafide(self, obj):
        return format_html('<a class="button" href="{}">Print</a>',
                           reverse('admin:print_bonafide_certificate', args=[obj.pk]))

    print_bonafide.short_description = 'Bonafide Certificate'
    print_bonafide.allow_tags = True

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^(?P<object_id>.+)/bonafide/$',
                self.admin_site.admin_view(self.print),
                name='print_bonafide_certificate',
            ),
        ]
        return custom_urls + urls

    def print(self, request, object_id, *args, **kwargs):
        return self.process_action(
            request=request,
            object_id=object_id
        )

    def process_action(self, request, object_id):
        return generate_bonafide(request, object_id)




    


