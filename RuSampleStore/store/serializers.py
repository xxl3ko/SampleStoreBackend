from rest_framework import serializers

from .models import Sample, Pack, Label, Relation


class RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = '__all__'


class SampleSerializer(serializers.ModelSerializer):
    # rels = RelationSerializer(many=True)

    # fav = serializers.CharField(source='rels.fav')

    class Meta:
        model = Sample
        fields = ['rels']
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
