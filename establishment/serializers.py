from rest_framework import serializers

from establishment.models import Establishment
from event.models import Event


class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = '__all__'
