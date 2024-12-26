from django.db import models

# Create your models here.
class Employee(models.Model):
     employee_id = models.IntegerField(unique=True)
     employee_name = models.CharField(max_length=100)
     gender = models.CharField(max_length=10)
     salary = models.FloatField()