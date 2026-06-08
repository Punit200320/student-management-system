import rest_framework
from rest_framework  import serializers

from .models import Student

class StudentSerializer(
    serializers.ModelSerializer
):
    
    class Meta:

        model = Student

        fields ='_all_'

from rest_framework import viewsets
from  .models import Student

from .serializers import(
    StudentSerializer
)

class StudentViewSet(
    viewsets.ModelViewSet
):
    
    queryset = (
        Student.objects.all()
    )

    serializer_class=(
        StudentSerializer
    )
from rest_framework.routers import(
    DefaultRouter
)

router = DefaultRouter()

router.register(
    'students-api',
    StudentViewSet
)

urlpatterns = []
urlpatterns += router.urls