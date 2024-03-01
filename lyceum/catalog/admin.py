from django.contrib import admin

import catalog.models


class MainImageAdminInline(admin.TabularInline):
    model = catalog.models.ItemMainImages
    extra = 1


class ImagesAdminInline(admin.StackedInline):
    model = catalog.models.ItemImages


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
    ]
    inlines = [
        MainImageAdminInline,
        ImagesAdminInline,
    ]
    filter_horizontal = [catalog.models.Item.tags.field.name]
    list_editable = [catalog.models.Item.is_published.field.name]
    list_display_links = [catalog.models.Item.name.field.name]


@admin.register(catalog.models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        catalog.models.Tag.name.field.name,
        catalog.models.Tag.is_published.field.name,
    ]
    list_editable = [catalog.models.Item.is_published.field.name]
    list_display_links = [catalog.models.Item.name.field.name]


@admin.register(catalog.models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        catalog.models.Category.name.field.name,
        catalog.models.Category.is_published.field.name,
    ]
    list_editable = [catalog.models.Item.is_published.field.name]
    list_display_links = [catalog.models.Item.name.field.name]


__all__ = []
