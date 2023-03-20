from django.contrib import admin
from .models import Sample, Genre, SamplePack, Label

# Register your models here.
admin.site.register(Sample)
admin.site.register(SamplePack)
admin.site.register(Genre)
admin.site.register(Label)
