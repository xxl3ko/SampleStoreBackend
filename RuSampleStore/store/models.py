from django.db import models


class Sample(models.Model):
    title = models.CharField(max_length=100)
    sample_pack = models.ForeignKey('SamplePack', default=None, null=True, on_delete=models.SET_NULL)
    genre = models.ForeignKey('Genre', default=None, null=True, on_delete=models.SET_NULL)
    file_src = models.FileField(upload_to='', null=True)

    def __str__(self):
        return self.title


class SamplePack(models.Model):
    title = models.CharField(max_length=100)
    cover_src = models.ImageField(upload_to='', null=True)

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
