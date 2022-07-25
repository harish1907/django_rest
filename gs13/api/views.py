from api.models import *
from api.serializers import *
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from api.custompermission import MyPermission


# Curd opration with respect to Default router.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]