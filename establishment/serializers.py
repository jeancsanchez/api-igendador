from rest_framework import serializers

from establishment.models import Establishment
from event.serializers import EventSerializer


class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = '__all__'


class EstablishmentFullSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Establishment
        fields = ('id', 'title', 'subtitle', 'owner', 'events')
