
from django.db import models
from courses.models import Course

class  Student(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    age = models.IntegerField()

    phone = models.CharField(max_length=15)

    address = models.TextField()

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='students'
    )

    created_at = models.DateField(
        auto_now_add=True
    )
    updated_at = models.DateField(
        auto_now=True
    )

    def _str_(self):
        return self.name
# Create your models here.
