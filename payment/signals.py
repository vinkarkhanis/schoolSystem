from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PaymentInfo
from studentinfo.models import Student

@receiver(post_save, sender=PaymentInfo)
def create_badge(sender, instance=None, created=False, **kwargs):
    if created:
        student, is_created = Student.objects.get_or_create(rollNum=instance.rollNum.rollNum,defaults={'count': 0})
        student.fees = student.fees-instance.payment
        student.save()
