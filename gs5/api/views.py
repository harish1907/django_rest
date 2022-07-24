from os import stat
from urllib import response
from django.urls import is_valid_path
from jmespath import search
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request, id=None):
    if request.method == "GET":
        id = request.data.get('id')
        if id:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response({'mssg':'Get data successfully', 'data': serializer.data})
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response({'mssg':'Get data successfully', 'data': serializer.data})
    
    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "PUT":
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response({'msg': 'Data Updated.'})
        return Response({'msg': serializer.errors})
