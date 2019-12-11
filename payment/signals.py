from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import PaymentInfo
from studentinfo.models import Student

@receiver(post_save, sender=PaymentInfo)
def create_badge(sender, instance=None, created=False, **kwargs):
    if created:
        student, is_created = Student.objects.get_or_create(rollNum=instance.rollNum.rollNum,std=instance.rollNum.std,
                                                            div=instance.rollNum.div)
        student.fees = student.fees-instance.payment
        if(student.fees == 0):
            student.total_fee_received = True;
        student.save()

@receiver(post_delete, sender=PaymentInfo)
def delete_badge(sender, instance=None, **kwargs):
    student, is_created = Student.objects.get_or_create(rollNum=instance.rollNum.rollNum,std=instance.rollNum.std,
                                                        div=instance.rollNum.div)
    student.fees = student.fees+instance.payment
    if(student.fees == 0):
        student.total_fee_received = True;
    elif(student.fees != 0):
        student.total_fee_received = False;

    student.save()

@receiver(pre_save, sender=PaymentInfo)
def update_badge(sender, instance=None, **kwargs):
        student, is_created = Student.objects.get_or_create(rollNum=instance.rollNum.rollNum,std=instance.rollNum.std,
                                                            div=instance.rollNum.div)
        try:
            payment_old = PaymentInfo.objects.get(pk=instance.pk)
            if payment_old is not None:
                update_payment=payment_old.payment - instance.payment
                student.fees = student.fees + update_payment
                if (student.fees == 0):
                    student.total_fee_received = True
                student.save()
        except:
            pass

