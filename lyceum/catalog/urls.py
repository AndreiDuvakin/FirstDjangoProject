from catalog import converters
from catalog import views
from django.urls import path, re_path, register_converter

register_converter(converters.CatalogIntConverter, "digit_to_convert")

urlpatterns = [
    path("", views.item_list),
    path("<int:item_id>/", views.item_detail),
    re_path(r"^re/(?P<number>\d+)/$", views.repeat_int),
    path("converter/<digit_to_convert:digit>/", views.redigit),
]
