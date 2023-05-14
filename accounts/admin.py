from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class AccountAdmin(UserAdmin):
    list_display = ("email", "first_name", "last_name", "last_login", "date_joined")
    list_display_links = ("email", "first_name", "last_name")
    readonly_fields = ("last_login", "date_joined")
    ordering = ("-date_joined",)

    fieldsets = ()


admin.site.register(User, AccountAdmin)
