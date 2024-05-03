from rest_framework import serializers

from ..models import Event


class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source="organizer.email")

    class Meta:
        model = Event
        fields = (
            "id",
            "organizer",
            "users",
            "title",
            "description",
            "date",
            "location",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {
            "organizer": {"read_only": True},
            "users": {"read_only": True},
        }
