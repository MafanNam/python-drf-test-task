from rest_framework import generics, permissions

from ..models import Event
from .serializers import EventSerializer
from ..permissions import OrganizerRequiredPermission


class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (permissions.AllowAny,)
        elif self.request.method == 'POST':
            self.permission_classes = (permissions.IsAuthenticated,)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (permissions.AllowAny,)
        else:
            self.permission_classes = (OrganizerRequiredPermission,)
        return super().get_permissions()


class EventRegisterUserAPIView(generics.CreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        event = self.get_object()
        event.users.add(request.user)
        return event
