from django.conf import settings
from django.core.mail import send_mail
from rest_framework import generics, permissions, status, views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from ..models import Event
from ..permissions import OrganizerRequiredPermission
from .serializers import EventSerializer


class EventListCreateAPIView(generics.ListCreateAPIView):
    """
    API view for listing and creating events.
    Only the organizer can create events.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = (permissions.AllowAny,)
        elif self.request.method == "POST":
            self.permission_classes = (permissions.IsAuthenticated,)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting event details.
    Details of an event by its ID.
    Only the organizer can update or delete the event.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = (permissions.AllowAny,)
        else:
            self.permission_classes = (OrganizerRequiredPermission,)
        return super().get_permissions()


class EventRegisterUserAPIView(views.APIView):
    """
    API view for registering users on events.
    Only the authenticated user can register on an event.
    """

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = None

    def post(self, request, *args, **kwargs) -> Response:
        user = request.user
        event = get_object_or_404(Event, id=kwargs.get("pk"))
        if event.organizer == user:
            return Response({"message": "You can not register on your own event"}, status=status.HTTP_400_BAD_REQUEST)
        if event.users.filter(id=user.id).exists():
            return Response({"message": "User already registered on event"}, status=status.HTTP_400_BAD_REQUEST)

        event.users.add(request.user)

        subject = f"Registration on event {event.title}"
        message = f"You have successfully registered for the event - {event.title} that will start at {event.date}"
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [user.email], fail_silently=True)

        return Response({"message": "User registered on event successfully"}, status=status.HTTP_200_OK)
