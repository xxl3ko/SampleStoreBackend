from django.db import models


class Sample(models.Model):
    title = models.TextField()
    genre = models.ForeignKey('Genre', default=None, null=True, on_delete=models.SET_NULL)
    instrument = models.CharField(max_length=255)
    artist = models.TextField()
    samplepack = models.TextField()

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
