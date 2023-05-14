from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    """
    Serializes Event data
    """

    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ("id", "created_by", "likes")

    def create(self, validated_data):
        event = Event.objects.create(**validated_data)
        return event
