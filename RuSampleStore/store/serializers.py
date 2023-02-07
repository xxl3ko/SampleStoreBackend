from rest_framework.serializers import ModelSerializer

from store.models import Sample


class SampleSerializer(ModelSerializer):

    class Meta:
        model = Sample
        fields = '__all__'
