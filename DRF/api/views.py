from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CreateUserSerializer
from .models import User

# Create your views here.

class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()



class RetrieveUpdateDestroyUserView(RetrieveUpdateDestroyAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()  