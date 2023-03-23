from django.contrib.auth.models import User
from django.db import models


class Sample(models.Model):
    title = models.CharField(max_length=100)
    label = models.ForeignKey('Label', null=True, on_delete=models.SET_NULL)
    pack = models.ForeignKey('Pack', related_name='samples', default=None, null=True,
                             on_delete=models.SET_NULL)
    genre = models.ForeignKey('Genre', default=None, null=True, on_delete=models.SET_NULL)
    file_src = models.FileField(upload_to='', null=True)
    users = models.ManyToManyField(User, through='Relation', related_name='suplex')
    objects = models.Manager()

    def __str__(self):
        return self.title


class Pack(models.Model):
    title = models.CharField(max_length=100)
    label = models.ForeignKey('Label', default=None, null=True, on_delete=models.SET_NULL)
    cover_src = models.ImageField(upload_to='', null=True)
    genre = models.ForeignKey('Genre', default=None, null=True, on_delete=models.SET_NULL)

    objects = models.Manager()

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.title



class Label(models.Model):
    title = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.title


class Relation(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    sample = models.ForeignKey(Sample, default=None, on_delete=models.CASCADE)
    fav = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return f'{self.user.username} | {self.sample.title}'
