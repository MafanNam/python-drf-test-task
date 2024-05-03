from django.test import TestCase
from ..models import Event
from ...users.tests.test_models import create_user
from datetime import datetime


class EventModelTests(TestCase):
    def test_str(self):
        """Test event string representation."""
        organizer = create_user('goood@email.com')
        event = Event.objects.create(title='Test event', organizer=organizer, date=datetime.now())
        self.assertEqual(str(event), f"{organizer.email} - {event.title}")
