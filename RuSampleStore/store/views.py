from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from .models import Sample, SamplePack
from .serializers import SampleSerializer, SamplePackSerializer


def main_page(request):
    return render(request, 'index.html', {'samples': Sample.objects.all})


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sample_pack']


class SamplePackViewSet(viewsets.ModelViewSet):
    queryset = SamplePack.objects.all()
    serializer_class = SamplePackSerializer
    permission_classes = [IsAuthenticated]
