from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..users.serializers import BaseUserModelSerializer

class LoginAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response(BaseUserModelSerializer(request.user).data, status=status.HTTP_200_OK)
