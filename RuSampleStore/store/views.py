from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import FileResponse
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
    serializer_class = SampleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Sample.objects.select_related('label', 'pack', 'genre').all().prefetch_related(
            Prefetch('rels', queryset=Relation.objects.filter(user=user).only('isFavorite', 'sample', 'user'))
        )


class PackViewSet(viewsets.ModelViewSet):
    # queryset = Pack.objects.all()
    serializer_class = PackSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Pack.objects.all().select_related('label', 'genre').prefetch_related(
            Prefetch('samples', queryset=Sample.objects.select_related('label', 'pack', 'genre').prefetch_related(
                Prefetch('rels', queryset=Relation.objects.filter(user=user).only('isFavorite', 'sample', 'user'))
            ))
        )


class RelationView(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
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


class DownloadSampleView(APIView):
    """ Скачивание сэмпла
    """

    def get(self, request, pk):
        sample = get_object_or_404(Sample, id=pk)
        user = self.request.user
        print(user)
        return FileResponse(
            open(sample.file.path, 'rb'), filename=sample.file.name, as_attachment=True
        )
