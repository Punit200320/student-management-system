from django.db.models.signals import (
    post_save,
    post_delete
)

from django.dispatch import receiver

from .models import Student

from audit.models import AuditLog

@receiver(
    post_save,
    sender=Student
)
def student_created(
    sender,
    instance,
    created,
    **kwargs
):
    
    if created:

        AuditLog.objects.create(
            action=
            f"{instance.name} created"
        )
    
@receiver(
    post_delete,
    sender=Student
)
def student_deleted(
    sender,
    instance,
    **kwargs
):
    
    AuditLog.objects.create(
        action=
        f"{instance.name} deleted"
    )