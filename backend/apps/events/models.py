from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Event(models.Model):
    """Event model"""

    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events_organizer")
    users = models.ManyToManyField(User, related_name="events", blank=True)
    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(max_length=1000, blank=True)
    date = models.DateField()

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")

    def __str__(self):
        return f"{self.organizer} - {self.title}"
