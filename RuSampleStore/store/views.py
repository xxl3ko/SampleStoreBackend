from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from store.models import Sample
from store.serializers import SampleSerializer


def main_page(request):
    return render(request, 'index.html', {'samples': Sample.objects.all})


class SampleView(ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
