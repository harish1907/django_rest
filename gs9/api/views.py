from api.models import *
from api.serializers import *
from rest_framework import viewsets


# Curd opration with respect to Default router.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer