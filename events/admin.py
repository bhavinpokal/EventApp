from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "time", "venue")
    list_filter = ("name", "date", "time", "venue", "created_by__email")
    list_display_links = ("name", "date", "time", "venue")
    readonly_fields = ("created_by", "likes")
    ordering = ("-date", "-time")

    filter_horizontal = ()


admin.site.register(Event, EventAdmin)
