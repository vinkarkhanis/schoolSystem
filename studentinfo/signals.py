from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Student, Fees

@receiver(post_save, sender=Student)
def create_badge(sender, instance=None, created=False, **kwargs):
    if created:
        fees, is_created = Fees.objects.get_or_create(std=instance.std )
        if(instance.exempt_fee == "Yes"):
            instance.fees = 0
            instance.total_fee_received = True
        elif(instance.exempt_fee == "No"):
            instance.fees = fees.fees
            instance.total_fee_received = False
        instance.save()

# @receiver(post_save, sender=Student)
# def update_badge(sender, instance=None, **kwargs):
#     student, is_created = Student.objects.get_or_create(rollNum=instance.rollNum, std=instance.std,
#                                                         div=instance.div)
#     fees, is_created = Fees.objects.get_or_create(std=instance.std)
#     try:
#         if(student.exempt_fee == "Yes"):
#             student.total_fee_received = True
#             student.fees = 0;
#         elif(student.exempt_fee == "No"):
#             student.total_fee_received = False
#             student.fees = fees.fees
#
#         student.save()
#     except:
#         pass
