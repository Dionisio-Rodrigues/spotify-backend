from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import MusicModelViewSet


router = DefaultRouter()
router.register(r'musics', MusicModelViewSet, 'musics')

urlpatterns = [
    path('', include(router.urls)),
]
