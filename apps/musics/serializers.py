from rest_framework import serializers
from .models import Music


class MusicModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        exclude = []
