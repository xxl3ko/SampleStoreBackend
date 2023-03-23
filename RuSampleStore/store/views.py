from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from .models import Sample, Pack, Label, Relation
from .serializers import SampleSerializer, PackSerializer, LabelSerializer, RelationSerializer


def main_page(request):
    return render(request, 'index.html', {'samples': Sample.objects.all})


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title']


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['sample_pack']


class PackViewSet(viewsets.ModelViewSet):
    queryset = Pack.objects.all()
    serializer_class = PackSerializer
    # permission_classes = [IsAuthenticated]


class RelationView(UpdateModelMixin, GenericViewSet):
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'sample'

    def get_object(self):
        obj, _ = Relation.objects.get_or_create(
            user=self.request.user,
            sample_id=self.kwargs['sample']
        )
        return obj
