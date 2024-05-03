from datetime import datetime

from django.test import TestCase

from ...users.tests.test_models import create_user
from ..models import Event


class EventModelTests(TestCase):
    def test_str(self):
        """Test event string representation."""
        organizer = create_user("goood@email.com")
        event = Event.objects.create(title="Test event", organizer=organizer, date=datetime.now())
        self.assertEqual(str(event), f"{organizer.email} - {event.title}")
