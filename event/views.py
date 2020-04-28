import copy
import types

from rest_framework import viewsets

from establishment.models import Establishment
from event.models import Event, Status
from event.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        new_request = types.SimpleNamespace()
        new_request.data = copy.copy(request.data)
        data = new_request.data

        if Establishment.objects.get(id=data['establishment']).owner.id == data['client']:
            new_request.data['status'] = Status.AVAILABLE

        return super(EventViewSet, self).create(new_request, args, kwargs)
