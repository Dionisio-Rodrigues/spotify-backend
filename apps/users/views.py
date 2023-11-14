from rest_framework import viewsets

from .serializers import BaseUserModelSerializer
from .models import BaseUser


class BaseUserModelViewSet(viewsets.ModelViewSet):
    queryset = BaseUser.objects.all()
    filter_backends = []
    permission_classes = []
    serializer_class = BaseUserModelSerializer
