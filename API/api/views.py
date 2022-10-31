# from urllib import response
# from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
# from .models import Lead, UserProfile,User
from .serializers import StudentSerializer
from .models import Student
# from rest_framework import status
# # Create your views here.
class StudentListView(ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class StudentCreateView(CreateAPIView):    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateView(UpdateAPIView):    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDeleteView(DestroyAPIView):    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer