from rest_framework import serializers
from api.models import *


class StudentSerializer(serializers.ModelSerializer):     
    class Meta:
        model = Student
        fields = ["name", "roll", "city"]