import datetime

from rest_framework import status
from rest_framework.test import APITestCase

from establishment.models import Establishment
from event.models import Status
from user.models import User


class EventTestCase(APITestCase):
    fixtures = ['users.json', 'establishments.json', 'events.json']

    # Here, when a client creates a new event, the event's status is Reserved
    def test_client_creates_new_event(self):
        establishment = Establishment.objects.first()
        user = User.objects.last()

        event = {
            'establishment': establishment.id,
            'description': 'Hear care',
            'date': datetime.datetime.now().timestamp(),
            'client': user.id
        }

        response = self.client.post('/v1/events', data=event, format='json')

        self.assertEquals(status.HTTP_201_CREATED, response.status_code)
        self.assertEquals(event['establishment'], int(response.data['establishment']))
        self.assertEquals(event['client'], int(response.data['client']))
        self.assertEquals(Status.RESERVED, int(response.data['status']))

    # Here, when the owner creates a new event, the event's status is Available
    def test_owner_creates_new_event(self):
        establishment = Establishment.objects.first()

        event = {
            'establishment': establishment.id,
            'description': 'Hear care',
            'date': datetime.datetime.now().timestamp(),
            'client': establishment.owner.id
        }

        response = self.client.post('/v1/events', data=event, format='json')

        self.assertEquals(status.HTTP_201_CREATED, response.status_code)
        self.assertEquals(event['establishment'], int(response.data['establishment']))
        self.assertEquals(event['client'], int(response.data['client']))
        self.assertEquals(Status.AVAILABLE, int(response.data['status']))
