from django.contrib import admin

import catalog.models


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "is_published",
    ]
    filter_horizontal = ["tags"]
    list_editable = ["is_published"]
    list_display_links = ["name"]


@admin.register(catalog.models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "is_published",
    ]
    list_editable = ["is_published"]
    list_display_links = ["name"]


@admin.register(catalog.models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "is_published",
    ]
    list_editable = ["is_published"]
    list_display_links = ["name"]
