from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Fee, StudentExtra

@receiver(post_save, sender=Fee)
def update_student_fees(sender, instance, **kwargs):
    # Get the updated class fee
    updated_fee = instance.amount
    
    # Update the fees for all students with the corresponding class
    students = StudentExtra.objects.filter(cl=instance.cl)
    for student in students:
        student.fee = updated_fee
        student.save()