from django.shortcuts import render
from rest_framework import generics

from .models import Sample, SamplePack
from .serializers import SampleSerializer, SamplePackSerializer


def main_page(request):
    return render(request, 'index.html', {'samples': Sample.objects.all})


class SampleView(generics.ListCreateAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
class SamplePackView(generics.ListCreateAPIView):
    queryset = SamplePack.objects.all()
    serializer_class = SamplePackSerializer