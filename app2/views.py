from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from rest_framework import *
from .models import Student
from .serializers import StudentSerializer,StudentModelSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def student_detail(req,pk=None):
    print(pk)
    if req.method == "GET":
        print(pk)
        if pk:
          print(pk)
          complex_data=Student.objects.get(pk=pk)
          serialized_data=StudentSerializer(complex_data)
        else:
          complex_data = Student.objects.all()
          serialized_data = StudentSerializer(complex_data,many=True)
        json=JSONRenderer().render(serialized_data.data)
        return HttpResponse(json,content_type = "application/json")
    
    if req.method == "POST":
        json = req.body
        stream = io.BytesIO(json)
        python_native = JSONParser().parse(stream)
        complex_data = StudentSerializer(data=python_native)
        if complex_data.is_valid():
           complex_data.save()
           msg={'msg':'data inserted'}
           return JsonResponse(msg)
        else:
           return JsonResponse(complex_data.errors)
    if req.method == "PUT":
        json = req.body
        stream = io.BytesIO(json)
        python_native = JSONParser().parse(stream)
        id=python_native.get('id')
        ins=Student.objects.get(pk=id)
        complex_data = StudentSerializer(data=python_native,instance=ins)
        if complex_data.is_valid():
           complex_data.save()
           msg={'msg':'data modified'}
           return JsonResponse(msg)
        else:
           return JsonResponse(complex_data.errors)
    if req.method == "DELETE":
       json=req.body
       stream = io.BytesIO(json)
       python_native = JSONParser().parse(stream)
       id=python_native.get('id')
       ins=Student.objects.get(pk=id)
       ins.delete()
       msg={'msg':'data deleted'}
       return JsonResponse(msg)

