from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics

from ..musics.serializers import MusicModelSerializer
from .serializers import PlaylistModelSerializer
from ..musics.models import Music
from .models import Playlist


class PlaylistModelViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistModelSerializer
    filter_backends = []
    permission_classes = []

    def get_queryset(self):
        playlist_qs = Playlist.objects.all()

        if self.request.user.is_anonymous:
            return playlist_qs.filter(user=None)
        
        return playlist_qs.filter(user=self.request.user)


class ListPlaylistMusicsAPIView(generics.ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicModelSerializer
    filter_backends = []
    permission_classes = []
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        if self.lookup_url_kwarg in self.kwargs:
            playlist = get_object_or_404(Playlist, id=self.kwargs[self.lookup_url_kwarg])
            return playlist.musics.all()
        return Music.objects.none()
