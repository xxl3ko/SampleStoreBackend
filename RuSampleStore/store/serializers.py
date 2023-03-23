from rest_framework import serializers

from .models import Sample, Pack, Label, Relation


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = '__all__'


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'


class PackSerializer(serializers.ModelSerializer):
    samples = SampleSerializer(many=True)

    class Meta:
        model = Pack
        fields = '__all__'
        depth = 1


class RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = ('sample', 'fav')
