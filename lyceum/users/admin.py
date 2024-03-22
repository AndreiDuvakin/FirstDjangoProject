from django.contrib import admin
import django.contrib.auth
from django.contrib.auth.admin import UserAdmin

import users.models

user = django.contrib.auth.get_user_model()
admin.site.unregister(user)


class ProfileInline(admin.TabularInline):
    can_delete = False
    model = users.models.Profile
    fields = [
        users.models.Profile.birthday.field.name,
        users.models.Profile.image.field.name,
        users.models.Profile.coffee_count.field.name,
    ]
    readonly_fields = [
        users.models.Profile.coffee_count.field.name,
    ]


@admin.register(user)
class UserAdmin(UserAdmin):
    inlines = [
        ProfileInline,
    ]


__all__ = []
