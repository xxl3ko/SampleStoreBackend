from django.contrib import admin
from .models import Sample, Genre, Pack, Label, UserSampleRelation

# Register your models here.
admin.site.register(Sample)
admin.site.register(Pack)
admin.site.register(Genre)
admin.site.register(Label)
admin.site.register(UserSampleRelation)
