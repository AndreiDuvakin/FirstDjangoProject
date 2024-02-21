from django.contrib import admin

import catalog.models
import core.models


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        core.models.AbstractRootModel.name.field.name,
        core.models.AbstractRootModel.is_published.field.name,
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
