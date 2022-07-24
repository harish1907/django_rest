# from os import set_inheritable
# from django.shortcuts import render
# import io
# from rest_framework.parsers import JSONParser
# from api.models import *
# from api.serializers import *
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse, JsonResponse

# def student_api(request):
#     if request.method == "GET":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')
        
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json', safe=False)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from api.models import *
from api.serializers import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@ method_decorator(csrf_exempt, name="dispatch")
class StudentView(APIView):
    serializer_class = StudentSerializer

    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            raise Http404


    def get(self, request, id=None):
        if id:
            stu = self.get_object(id=id)        
            serializer = StudentSerializer(stu)
        
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            
        return Response({"message": "Records getting successfully.", "data": serializer.data}, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Records updated successfully.", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "something went wrong", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):
        instance = self.get_object(id)
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Records updated successfully.", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": "something went wrong", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        instance = self.get_object(id)
        instance.delete()
        return Response({"message": "Records deleted successfully."}, status=status.HTTP_204_NO_CONTENT)