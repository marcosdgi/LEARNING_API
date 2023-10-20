from django.urls import path 
from .API import students_api_view, students_datail_api_view
urlpatterns = [
    path('students/', students_api_view , name = 'Students'),
    path('students/<pk:int>/',students_datail_api_view,name = 'students_detail'),
]