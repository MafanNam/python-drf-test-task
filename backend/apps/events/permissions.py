from rest_framework import permissions


class OrganizerRequiredPermission(permissions.IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.organizer == request.user
