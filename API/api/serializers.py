from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Agent    
User = get_user_model()

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','is_organizer','is_agent']

class AgentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['user','organizations']
