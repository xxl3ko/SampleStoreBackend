from django.contrib import admin
from .models import Sample, Genre, Pack, Label, Relation, Instrument, User

# Register your models here.
admin.site.register(User)
admin.site.register(Label)
admin.site.register(Pack)
admin.site.register(Sample)
admin.site.register(Instrument)
admin.site.register(Genre)
admin.site.register(Relation)
