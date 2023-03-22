from django.contrib import admin
from .models import Sample, Genre, Pack, Label

# Register your models here.
admin.site.register(Sample)
admin.site.register(Pack)
admin.site.register(Genre)
admin.site.register(Label)
