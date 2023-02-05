from django.shortcuts import render
from rest_framework import generics

from store.models import Sample
from store.serializers import SampleSerializer


def main_page(request):
    return render(request, 'index.html', {'samples': Sample.objects.all})


class SampleView(generics.ListCreateAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
