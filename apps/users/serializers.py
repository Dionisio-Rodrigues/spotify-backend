from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import BaseUser



class BaseUserModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BaseUser
        fields = '__all__'

    def save(self, **kwargs):
        if "password" in self.validated_data:
            self.validated_data["password"] = make_password(self.validated_data["password"])
        return super().save(**kwargs)
