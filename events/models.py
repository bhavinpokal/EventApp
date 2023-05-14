from django.conf import settings
from django.db import models


class Event(models.Model):
    """
    Stores an event using :model:`events.Event`
    """

    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=200)
    image = models.ImageField(upload_to="events/", blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="events"
    )
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="liked_events", blank=True
    )

    def __str__(self):
        return self.name
