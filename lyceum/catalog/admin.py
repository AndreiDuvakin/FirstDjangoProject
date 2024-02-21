from django.contrib import admin

import catalog.models
import core.models


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        core.models.AbstractRootModel.name.field.name,
        core.models.AbstractRootModel.is_published.field.name,
    ]
    filter_horizontal = [catalog.models.Item.tags.field.name]
    list_editable = [core.models.AbstractRootModel.is_published.field.name]
    list_display_links = [core.models.AbstractRootModel.name.field.name]


@admin.register(catalog.models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        core.models.AbstractRootModel.name.field.name,
        core.models.AbstractRootModel.is_published.field.name,
    ]
    list_editable = [core.models.AbstractRootModel.is_published.field.name]
    list_display_links = [core.models.AbstractRootModel.name.field.name]


@admin.register(catalog.models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        core.models.AbstractRootModel.name.field.name,
        core.models.AbstractRootModel.is_published.field.name,
    ]
    list_editable = [core.models.AbstractRootModel.is_published.field.name]
    list_display_links = [core.models.AbstractRootModel.name.field.name]
