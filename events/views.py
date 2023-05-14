from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Event
from .serializers import EventSerializer


class CreateEventAPIView(APIView):
    """
    Creates an event
    """

    permission_classes = (IsAuthenticated,)
    template_name = "events/createEvent.html"

    def get(self, request):
        """
        Returns CreateEvent HTML template
        """
        return render(request, self.template_name)

    def post(self, request, format=None):
        """
        On POST request, creates event
        """
        serializer = EventSerializer(data=request.data, context={"request": request})

        if serializer.is_valid():
            event = serializer.save(created_by=request.user)
            event.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllEventListAPIView(APIView):
    """
    Displays all events
    """

    permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "events/allEvents.html"

    def get(self, request):
        events = Event.objects.all()
        liked_events = request.user.liked_events.all()
        return Response(
            {"events": events, "liked_events": liked_events},
            template_name=self.template_name,
        )


class UserEventListAPIView(APIView):
    """
    Displays events created by the currently authorized/logged in user
    """

    permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "events/userEvents.html"

    def get(self, request):
        events = Event.objects.filter(created_by=request.user)
        return Response({"events": events}, template_name=self.template_name)


class EventLikeAPIView(APIView):
    """
    Handles like-unlike of the event if the user is authorized
    """

    permission_classes = (IsAuthenticated,)

    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        user = request.user

        if user in event.likes.all():
            event.likes.remove(user)
            return Response({"liked": False}, status=status.HTTP_200_OK)
        else:
            event.likes.add(user)
            return Response({"liked": True}, status=status.HTTP_200_OK)


class EventDeleteView(APIView):
    """
    Deletes an event
    """

    permission_classes = (IsAuthenticated,)

    def delete(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)

        if request.user != event.created_by:
            return Response(
                {"error": "You do not have permission to delete this event."},
                status=status.HTTP_403_FORBIDDEN,
            )
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EventUpdateAPIView(APIView):
    """
    Provides event update view and handles event updation
    """

    permission_classes = (IsAuthenticated,)
    template_name = "events/editEvent.html"

    def get(self, request, event_id, format=None):
        """
        Displays event form with pre-populated data
        """
        event = get_object_or_404(Event, id=event_id)
        serializer = EventSerializer(instance=event)

        if request.user == event.created_by:
            return render(
                request,
                self.template_name,
                {"event": serializer.data, "imgName": serializer.data["image"][14:]},
            )
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, event_id, format=None):
        """
        Updates event
        """
        event = get_object_or_404(Event, id=event_id)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
