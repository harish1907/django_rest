from rest_framework import serializers
from api.models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name", "roll", "city"]
    
    # def create(self, validate_data):
    #     return Student.objects.create(**validate_data)