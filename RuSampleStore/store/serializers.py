from rest_framework import serializers

from .models import Sample, Pack, Label, Relation


class RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = ['fav']


class SampleSerializer(serializers.ModelSerializer):
    rels = RelationSerializer(many=True)

    class Meta:
        model = Sample
        fields = '__all__'
        depth = 1


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
