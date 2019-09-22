from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student, Fees

@receiver(post_save, sender=Student)
def create_badge(sender, instance=None, created=False, **kwargs):
    if created:
        fees, is_created = Fees.objects.get_or_create(std=instance.std )
        instance.fees=fees.fees
        instance.save()