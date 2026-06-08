from django.db import models

# Create your models here.
class Course(models.Model):

    name = models.CharField(max_length=100)

    duration = models.CharField(max_length=50)

    fees = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def _str_(self):
        return self.name
    