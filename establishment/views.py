# Create your views here.
from rest_framework import viewsets

from establishment.models import Establishment
from establishment.serializers import EstablishmentSerializer, EstablishmentFullSerializer


class EstablishmentViewSet(viewsets.ModelViewSet):
    queryset = Establishment.objects.prefetch_related('events').all()
    serializer_class = EstablishmentSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return EstablishmentFullSerializer
        return self.serializer_class
