from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "organizer", "title", "date", "location", "created_at")
    list_display_links = ("id", "organizer", "title")
    list_filter = ("organizer", "date", "location")
    ordering = ("-created_at",)
    search_fields = ("title", "organizer__username")
