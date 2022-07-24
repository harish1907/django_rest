from api.models import *
from api.serializers import *
from rest_framework import viewsets


# Curd opration with respect to Default router.
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer