from rest_framework import viewsets, filters

from .serializers import MusicModelSerializer
from .models import Music


class MusicModelViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = []
