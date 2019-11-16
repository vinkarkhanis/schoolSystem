from django.conf.urls import url
from django.contrib import admin, messages
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse, path
from django.utils.html import format_html

from studentinfo.models import Student

from studentinfo.views import GeneratePdf

from studentinfo import views
from .models import PaymentInfo
from import_export.admin import ImportExportModelAdmin

class InputFilter(admin.SimpleListFilter):
    template = 'admin/input_filter.html'
    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ((),)

    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice

class DateFilter(InputFilter):
    parameter_name = 'dateTxn'
    title = ('Date of Transaction')

    def queryset(self, request, queryset):
        if self.value() =='29':
            messages.error(request,"Please enter Date in format : YYYY-MM-DD")
            render(request,'admin/input_filter.html')
        elif self.value() is not None:
            dateTxn = self.value()
            return queryset.filter(
                Q(dateTxn=dateTxn)

            )

# admin.site.register(PaymentInfo)
@admin.register(PaymentInfo)
class PaymentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    autocomplete_fields = ("rollNum",)
    list_display = ('roll_no','name','last_name','payment','dateTxn','Class','print_receipt',)
    search_fields = ('rollNum__rollNum',)
    list_filter=(DateFilter,)
    # fields = (
    #      'Student_rollNum',
    # )
    _roll_no = 0

    def Class(self,obj):
        return "{} {}".format(obj.rollNum.std,obj.rollNum.div)

    def name(self,obj):
        return "{}".format(obj.rollNum.first_name)

    def last_name(self, obj):
        return "{}".format(obj.rollNum.last_name)

    def roll_no(self,obj):
        _roll_no = obj.rollNum.rollNum
        return _roll_no

    roll_no.admin_order_field = 'rollNum'

    def print_receipt(self, obj):
        return format_html('<a class="button" href="{}">Print</a>',
                            reverse('admin:payment_receipt',args=[obj.pk]))

    print_receipt.short_description = 'Print Receipt'
    print_receipt.allow_tags = True

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                 r'^(?P<object_id>.+)/print/$',
                self.admin_site.admin_view(self.print),
                name='payment_receipt',
            ),
        ]
        return custom_urls + urls

    def print(self, request, object_id, *args, **kwargs):
        return self.process_action(
            request=request,
            object_id=object_id
        )

    def process_action(self, request,object_id):
        return GeneratePdf(request,object_id)

