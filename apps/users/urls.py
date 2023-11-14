from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import BaseUserModelViewSet


router = DefaultRouter()
router.register(r'users', BaseUserModelViewSet, 'users')

urlpatterns = [
    path('', include(router.urls))
]
