from rest_framework import serializers

from daybook.models import DayBook
from establishment.models import Establishment
from event.models import Event


class DayBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayBook
        fields = '__all__'
        depth = 1
