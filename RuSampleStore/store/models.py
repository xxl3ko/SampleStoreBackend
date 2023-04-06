from django.contrib.auth.models import User
from django.db import models

from base.services import get_path_upload_sample, get_path_upload_cover


class Relation(models.Model):
    objects = models.Manager()

    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    sample = models.ForeignKey('Sample', default=None, related_name='rels', on_delete=models.CASCADE)

    fav = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} | {self.sample.title} | Fav: {self.fav}'


class Sample(models.Model):
    objects = models.Manager()

    TYPE_CHOICES = [
        ('One Shot', 'One Shot'),
        ('loop', 'Loop')
    ]

    name = models.CharField(max_length=100)
    label = models.ForeignKey('Label', null=True, on_delete=models.SET_NULL)
    pack = models.ForeignKey('Pack',
                             related_name='samples',
                             default=None,
                             null=True,
                             on_delete=models.SET_NULL
                             )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, null=True, default=None)
    genre = models.ForeignKey('Genre', default=None, null=True, on_delete=models.SET_NULL)
    tempo = models.PositiveIntegerField(default=None, null=True)
    file = models.FileField(upload_to=get_path_upload_sample,
                            null=True
                            )

    # users = models.ManyToManyField(User, through='Relation', related_name='suplex')

    def __str__(self):
        return f'{self.id}: {self.name}'


class Pack(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=100)
    label = models.ForeignKey('Label', default=None, null=True, on_delete=models.SET_NULL)
    cover = models.ImageField(upload_to=get_path_upload_cover, null=True)
    genre = models.ForeignKey('Genre', default=None, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Genre(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name
