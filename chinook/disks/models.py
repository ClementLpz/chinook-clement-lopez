from django.db import models

# Create your models here.

class Artist(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Album(models.Model):

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Track(models.Model):

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=200)
    milliseconds = models.IntegerField(default=0)
    bytes = models.IntegerField(default=0)
    unitPrice = models.FloatField(default=0.0)

    def __str__(self):
        return self.question_text
