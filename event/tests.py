import datetime

from rest_framework import status
from rest_framework.test import APITestCase

from daybook.models import DayBook
from daybook.serializers import DayBookSerializer
from establishment.models import Establishment


class EventTestCase(APITestCase):

    def test_create_new_event(self):
        establishment = Establishment.objects.create(title='Shop')
        day_book = DayBook.objects.create(date=datetime.datetime.now(), establishment=establishment)

        event = {
            'day_book': day_book.id,
            'description': 'Barber shop',
            'hour': datetime.datetime.now().timestamp()
        }

        response = self.client.post('/v1/events', data=event, format='json')

        self.assertEquals(status.HTTP_201_CREATED, response.status_code)
