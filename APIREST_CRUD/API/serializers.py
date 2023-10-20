from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User 

class StudentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = '__all__'


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'