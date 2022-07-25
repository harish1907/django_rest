from api.models import *
from api.serializers import *
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


# Curd opration with respect to Default router.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # Basic authentication perticular class
    # authentication_classes = [BaseAuthentication]
    # permission_classes = [IsAuthenticated]
    
    
    # Overwrigth global authentication
    # authentication_classes = [BaseAuthentication]
    # permission_classes = [AllowAny]
    
    
    # Only use staff and admin this permission not allowed to user by local user.
    # permission_classes = [IsAdminUser]
    