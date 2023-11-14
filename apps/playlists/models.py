from django.db import models


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    musics = models.ManyToManyField('musics.Music', blank=True)
    cover = models.ImageField(upload_to='images')
    user = models.ForeignKey('users.BaseUser', on_delete=models.CASCADE, null=True, blank=True)
