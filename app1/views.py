
from django.http import JsonResponse,HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

from .models import Employee
from .serializers import EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def home(req):
    if req.method == "GET":
        data=Employee.objects.all() # complex_data_get
        serialized=EmployeeSerializer(data,many=True) # make them python native 
        print(serialized)
        print(serialized.data)
        json= JSONRenderer().render(serialized.data)  # convert_them_into_json
        #return JsonResponse(serialized.data,safe=False)
        return HttpResponse(json,content_type="application/json")
        #return HttpResponse(json,content_type="application/json")
    

    if req.method == "POST":
        data = req.body # getting data from url(with req)
        stream= io.BytesIO(data)
        python_native = JSONParser().parse(stream)
        deserialized_data = EmployeeSerializer(data=python_native)
        if deserialized_data.is_valid():
            deserialized_data.save()
            msg = {'msg': 'record inserted'}
            return JsonResponse(msg)


