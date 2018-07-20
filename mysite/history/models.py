from django.db import models


class Artist(models.Model):
    name_text = models.CharField(max_length=200)



class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title_text = models.CharField(max_length=200)
