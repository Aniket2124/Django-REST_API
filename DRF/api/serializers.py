from rest_framework import serializers
from .models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','display_name','description','creation_time']
        read_only_fields = ['creation_time']        
       