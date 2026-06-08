from django.db import models

# Create your models here.

class AuditLog(models.Model):     
    action = models.CharField(
        max_length=255
    )

    timestamp = models.DateField(
        auto_now_add=True
    )
    
    def _str_(self):
        return self.action
