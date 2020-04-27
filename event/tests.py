import datetime

from rest_framework import status
from rest_framework.test import APITestCase

from daybook.models import DayBook
from establishment.models import Establishment
from user.models import User


class EventTestCase(APITestCase):

    def test_create_new_event(self):
        establishment = Establishment.objects.create(title='Shop')
        day_book = DayBook.objects.create(date=datetime.datetime.now(), establishment=establishment)
        user = User.objects.create_user(email='email@email.com', name='fake', password='qwer')

        event = {
            'day_book': day_book.id,
            'description': 'Barber shop',
            'hour': datetime.datetime.now().timestamp(),
            'user': user.id
        }

        response = self.client.post('/v1/events', data=event, format='json')

        self.assertEquals(status.HTTP_201_CREATED, response.status_code)
