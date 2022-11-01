# from urllib import response
# from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
# from .models import Lead, UserProfile,User
from .serializers import StudentSerializer
from .models import Student
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
# from rest_framework import status
# # Create your views here.
class StudentListView(ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
# ------------------Added basic authentication--------------------------
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
#----- -----------Any one can access the api -------------------------
#     permission_classes = [AllowAny]
# # ------------------Only Staff user status ia active an access ---------------
#     permission_classes = [IsAdminUser]


class StudentCreateView(CreateAPIView):    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateView(UpdateAPIView):    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDeleteView(DestroyAPIView):    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer