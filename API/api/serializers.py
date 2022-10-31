from rest_framework import serializers
# # from django.contrib.auth import get_user_model
from .models import Student  
# # User = get_user_model()

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','roll','city',]

# class StudentCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'
