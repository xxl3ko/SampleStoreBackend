from django.db import models


class Sample(models.Model):
    title = models.TextField()
    genre = models.CharField(max_length=255)
    instrument = models.CharField(max_length=255)
    artist = models.TextField()
    samplepack = models.TextField()

    def __str__(self):
        return self.title
