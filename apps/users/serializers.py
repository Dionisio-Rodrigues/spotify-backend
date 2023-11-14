from rest_framework import serializers
from .models import BaseUser


class BaseUserModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BaseUser
        fields = '__all__'
