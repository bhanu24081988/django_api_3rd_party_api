from rest_framework import serializers
from .models  import Student

class StudentSerializer(serializers.Serializer):
    roll=serializers.IntegerField()
    name=serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.roll=validated_data.get('roll',instance.roll)
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        return instance


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"