from django.urls import path, re_path, register_converter

from catalog import converters
from catalog import views

register_converter(converters.CatalogIntConverter, "digit_to_convert")

app_name = "catalog"

urlpatterns = [
    path("", views.item_list, name="item_list"),
    path("<int:item_id>/", views.item_detail, name="item"),
    path("new/", views.new_items, name="new_items"),
    path("friday/", views.friday_items, name="friday_items"),
    path("unverified/", views.unverified_items, name="unverified_items"),
    re_path(r"^re/(?P<number>\d+)/$", views.repeat_int, name="re_number"),
    path(
        "converter/<digit_to_convert:digit>/",
        views.redigit,
        name="converter",
    ),
]
