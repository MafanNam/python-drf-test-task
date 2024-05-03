from django.urls import path

from . import views

urlpatterns = [
    path("", views.EventListCreateAPIView.as_view(), name="event-list-create"),
    path("<int:pk>/", views.EventDetailAPIView.as_view(), name="event-detail"),
    path("<int:pk>/register/", views.EventRegisterUserAPIView.as_view(), name="event-register-user"),
]
