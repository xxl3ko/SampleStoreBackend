from django.db import models


class Sample(models.Model):
    title = models.CharField(max_length=100)
    label = models.ForeignKey('Label', null=True, on_delete=models.SET_NULL)
    pack = models.ForeignKey('Pack', related_name='samples', default=None, null=True,
                                    on_delete=models.SET_NULL)
    genre = models.ForeignKey('Genre', default=None, null=True, on_delete=models.SET_NULL)
    file_src = models.FileField(upload_to='', null=True)

    def __str__(self):
        return self.title


class Pack(models.Model):
    title = models.CharField(max_length=100)
    label = models.ForeignKey('Label', default=None, null=True, on_delete=models.SET_NULL)
    cover_src = models.ImageField(upload_to='', null=True)
    genre = models.ForeignKey('Genre', default=None, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Label(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
