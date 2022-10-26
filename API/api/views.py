from urllib import response
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Lead, UserProfile,User
from .serializers import LeadSerializer, AgentCreateSerializer
from rest_framework import status
# Create your views here.
class LeadListView(ListAPIView):
    serializer_class = LeadSerializer
    queryset = User.objects.all()

class LeadCreateView(CreateAPIView):    
    queryset = User.objects.all()
    serializer_class = AgentCreateSerializer