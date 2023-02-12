from rest_framework.serializers import ModelSerializer

from .models import Sample, SamplePack


class SampleSerializer(ModelSerializer):
    class Meta:
        model = Sample
        fields = '__all__'

class SamplePackSerializer(ModelSerializer):
    class Meta:
        model = SamplePack
        fields = '__all__'
