from django.contrib import admin
from .models import Sample, Genre, SamplePack

# Register your models here.
admin.site.register(Sample)
admin.site.register(SamplePack)
admin.site.register(Genre)
