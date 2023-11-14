from rest_framework import serializers
from .models import Playlist


class PlaylistModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playlist
        exclude = []
