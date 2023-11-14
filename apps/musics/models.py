from django.db import models


class Music(models.Model):
    audio = models.FileField(upload_to='musics')
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
