from rest_framework import serializers

from .models import Sample, SamplePack, Label


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = '__all__'


class SamplePackSerializer(serializers.ModelSerializer):
    samples = serializers.StringRelatedField(many=True)

    class Meta:
        model = SamplePack
        fields = '__all__'


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'
