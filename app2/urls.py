from django.urls import include,path
from . import views


urlpatterns =[
   path("",views.student_detail),
   path("get/<pk>/",views.student_detail),

]