from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from ...users.tests.test_models import create_user
from ..models import Event

EVENT_LIST_CREATE_URL = reverse("events:event-list-create")


def detail_event_url(event_id):
    """Event detail URL."""
    return reverse("events:event-detail", args=[event_id])


def event_register_user_url(event_id):
    """Event register user URL."""
    return reverse("events:event-register-user", args=[event_id])


class PublicTestEventViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = create_user(is_active=True)
        self.event1 = Event.objects.create(
            title="test event",
            description="test description",
            date="2024-01-01",
            organizer=self.user1,
        )

    def test_list_events(self):
        res = self.client.get(EVENT_LIST_CREATE_URL)
        self.assertEqual(res.status_code, 200)

    def test_create_event_unauthorized(self):
        payload = {
            "title": "string",
            "description": "string",
            "organizer": self.user1.id,
            "date": "2024-01-02",
        }

        res = self.client.post(EVENT_LIST_CREATE_URL, payload)
        self.assertEqual(res.status_code, 401)

    def test_detail_event(self):
        res = self.client.get(detail_event_url(self.event1.id))
        self.assertEqual(res.status_code, 200)


class PrivateTestAuthenticationViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = create_user()
        self.user2 = create_user(email="test2@gmail.com")
        self.client.force_authenticate(self.user1)
        self.event1 = Event.objects.create(
            title="test event",
            description="test description",
            date="2024-01-01",
            organizer=self.user1,
        )
        self.event2 = Event.objects.create(
            title="test event2",
            description="test description",
            date="2024-01-05",
            organizer=self.user2,
        )

    def test_detail_event(self):
        res = self.client.get(detail_event_url(self.event1.id))
        self.assertEqual(res.status_code, 200)

        res = self.client.get(detail_event_url(self.event2.id))
        self.assertEqual(res.status_code, 200)

    def test_create_event(self):
        payload = {
            "title": "string",
            "description": "string",
            "organizer": self.user1.id,
            "date": "2024-01-02",
        }

        res = self.client.post(EVENT_LIST_CREATE_URL, payload)
        self.assertEqual(res.status_code, 201)

    def test_update_event(self):
        payload = {
            "title": "stringNew",
            "description": "stringNew",
            "date": "2024-01-02",
        }

        # patch
        res = self.client.patch(detail_event_url(self.event1.id), payload, format="json")
        self.assertEqual(res.status_code, 200)

        # put
        res = self.client.put(detail_event_url(self.event1.id), payload, format="json")
        self.assertEqual(res.status_code, 200)

    def test_delete_event(self):
        res = self.client.delete(detail_event_url(self.event1.id))
        self.assertEqual(res.status_code, 204)

    def test_event_register_user(self):
        payload = {"event": self.event1.id}

        # cannot register on own event
        res = self.client.post(event_register_user_url(self.event1.id), payload, format="json")
        self.assertEqual(res.status_code, 400)

        # can register on other event
        self.client.force_authenticate(self.user2)
        res = self.client.post(event_register_user_url(self.event1.id), payload, format="json")
        self.assertEqual(res.status_code, 200)

        # cannot register twice
        res = self.client.post(event_register_user_url(self.event1.id), payload, format="json")
        self.assertEqual(res.status_code, 400)
