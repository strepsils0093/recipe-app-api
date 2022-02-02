from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core_app import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    list_filter = ['is_staff']
    fieldsets = (
        (None, ),
        (),
        (),
        ()

    )


admin.site.register(models.User, UserAdmin)
