from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import PlaylistModelViewSet, ListPlaylistMusicsAPIView


router = DefaultRouter()
router.register(r'playlists', PlaylistModelViewSet, 'playlists')

urlpatterns = [
    path('', include(router.urls)),
    path('playlists/<int:pk>/musics', ListPlaylistMusicsAPIView.as_view())
]
