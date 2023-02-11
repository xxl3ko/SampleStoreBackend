from django.shortcuts import render
from rest_framework import generics

from .models import Sample
from .serializers import SampleSerializer


def main_page(request):
    return render(request, 'index.html', {'samples': Sample.objects.all})


class SampleView(generics.ListCreateAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
