from django.contrib import admin

import catalog.models


class ItemAdminInline(admin.TabularInline):
    model = catalog.models.Item
    extra = 1


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
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


@admin.register(catalog.models.ItemMainImages)
class MainImagesAdmin(admin.ModelAdmin):
    list_display = [catalog.models.ItemMainImages.main_image.field.name]
    inlines = [
        ItemAdminInline,
    ]


@admin.register(catalog.models.ItemImages)
class ImagesAdmin(admin.ModelAdmin):
    list_display = [catalog.models.ItemImages.image.field.name]


__all__ = [
    ItemAdmin,
    TagAdmin,
    CategoryAdmin,
    MainImagesAdmin,
    ImagesAdmin,
]
