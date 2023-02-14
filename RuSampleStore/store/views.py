from django.shortcuts import render
from rest_framework import generics, viewsets

from .models import Sample, SamplePack
from .serializers import SampleSerializer, SamplePackSerializer


def main_page(request):
    return render(request, 'index.html', {'samples': Sample.objects.all})


class SampleView(generics.ListCreateAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class SamplePackViewSet(viewsets.ModelViewSet):
    queryset = SamplePack.objects.all()
    serializer_class = SamplePackSerializer
