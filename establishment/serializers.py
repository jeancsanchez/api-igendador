from rest_framework import serializers

from establishment.models import Establishment, Availability
from event.serializers import EventSerializer


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'


class EstablishmentSerializer(serializers.ModelSerializer):
    photos = serializers.StringRelatedField(many=True)
    availability = AvailabilitySerializer(read_only=True)

    class Meta:
        model = Establishment
        fields = ('id', 'title', 'subtitle', 'owner', 'availability', 'photos',)


class EstablishmentWithEventsSerializer(serializers.ModelSerializer):
    photos = serializers.StringRelatedField(many=True)
    availability = AvailabilitySerializer(read_only=True)
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Establishment
        fields = ('id', 'title', 'subtitle', 'owner', 'availability', 'photos', 'events',)
