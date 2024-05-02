from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('organizer', 'title', 'date', 'created_at')
    list_display_links = ('organizer', 'title')
    list_filter = ('organizer', 'date')
    ordering = ('-created_at',)
    search_fields = ('title', 'organizer__username')
