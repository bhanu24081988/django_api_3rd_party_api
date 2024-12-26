from rest_framework import serializers
from .models import Employee



class EmployeeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeSerializer(serializers.Serializer):
    employee_id = serializers.IntegerField()
    employee_name = serializers.CharField(max_length=100)
    gender = serializers.CharField(max_length=10)
    salary = serializers.FloatField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.employee_id = validated_data.get('employee_id',instance.employee_id)
        instance.employee_name = validated_data.get('employee_name',instance.employee_name)
        instance.gender = validated_data.get('gender',instance.gender)
        instance.salary = validated_data.get('salary',instance.salary)
        instance.save()
        return instance