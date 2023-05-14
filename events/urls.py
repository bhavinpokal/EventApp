from django.urls import path

from .views import (
    AllEventListAPIView,
    CreateEventAPIView,
    EventDeleteView,
    EventLikeAPIView,
    EventUpdateAPIView,
    UserEventListAPIView,
)

urlpatterns = [
    path("create-event/", CreateEventAPIView.as_view(), name="create_event"),
    path("user-events/", UserEventListAPIView.as_view()),
    path("user-events/<int:event_id>/delete/", EventDeleteView.as_view()),
    path("all-events/", AllEventListAPIView.as_view()),
    path("all-events/<int:event_id>/", EventLikeAPIView.as_view()),
    path("edit-event/<int:event_id>/", EventUpdateAPIView.as_view()),
]
