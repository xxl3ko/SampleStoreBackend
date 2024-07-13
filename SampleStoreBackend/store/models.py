from django.contrib.auth.models import AbstractUser
from django.db import models

from base.services import get_path_upload_sample, get_path_upload_cover


class User(AbstractUser):
    score = models.IntegerField(null=True)


class BuyingSample(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    sample = models.ForeignKey('Sample', default=None, on_delete=models.CASCADE)
    isPurchased = models.BooleanField(default=False)


class Relation(models.Model):
    """Отношение между пользователем и сэмплом (Избранное)"""
    objects = models.Manager()

    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    sample = models.ForeignKey('Sample', default=None, related_name='rels', on_delete=models.CASCADE)
    isFavorite = models.BooleanField(default=False)
    isPurchased = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} | {self.sample.name} | Fav: {self.isFavorite}'


class Sample(models.Model):
    """Сэмпл - основная единица проекта"""
    objects = models.Manager()

    TYPE_CHOICES = [
        ('One Shot', 'One Shot'),
        ('loop', 'Loop')
    ]

    name = models.CharField(max_length=100)
    label = models.ForeignKey('Label', null=True, on_delete=models.SET_NULL)
    pack = models.ForeignKey('Pack', related_name='samples', null=True, default=None, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, null=True, default=None)
    instrument = models.ForeignKey('Instrument', null=True, blank=True, default=None, on_delete=models.SET_NULL)
    genre = models.ForeignKey('Genre', default=None, null=True, on_delete=models.SET_NULL)
    tempo = models.PositiveIntegerField(default=None, null=True, blank=True)
    file = models.FileField(upload_to=get_path_upload_sample, null=True)
    price = models.PositiveIntegerField(default=None, null=True)

    # users = models.ManyToManyField(User, through='Relation', related_name='suplex')

    def __str__(self):
        return f'{self.id}: {self.pack} - {self.name}'


class Pack(models.Model):
    """Сэмплпак который содержит в себе сэмплы"""
    objects = models.Manager()

    name = models.CharField(max_length=100)
    description = models.TextField(default=None, null=True)
    label = models.ForeignKey('Label', default=None, null=True, on_delete=models.SET_NULL)
    cover = models.ImageField(upload_to=get_path_upload_cover, null=True)
    genre = models.ForeignKey('Genre', default=None, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.label} - {self.name}'


class Genre(models.Model):
    """Жанр сэмпла"""
    objects = models.Manager()

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Label(models.Model):
    """Лэйбл кому принадлежит сэмпл"""
    name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Instrument(models.Model):
    """Инструмент который звучит в сэмпле"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}: {self.name}'
