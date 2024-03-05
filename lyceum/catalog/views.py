import datetime

import django.db.models
from django.http import HttpResponse
import django.shortcuts
import django.template.loader

import catalog.models


def item_list(request):
    template = django.template.loader.get_template("catalog/item_list.html")
    items = catalog.models.Item.objects.published().order_by("category__name")
    return HttpResponse(
        template.render(
            {"items": items, "title": "Каталог товаров"},
            request,
        ),
    )


def item_detail(request, item_id):
    template = django.template.loader.get_template("catalog/item.html")
    item = django.shortcuts.get_object_or_404(
        catalog.models.Item.objects.published(),
        pk=item_id,
    )
    return HttpResponse(
        template.render({"item": item, "title": "Просмотр товара"}, request),
    )


def repeat_int(request, number):
    return HttpResponse(number)


def redigit(request, digit):
    return HttpResponse(digit)


def new_items(request):
    template = django.template.loader.get_template("catalog/item_list.html")
    items = catalog.models.Item.objects.published().filter(
        created_date__gte=datetime.datetime.now() - datetime.timedelta(days=7),
    )
    return HttpResponse(
        template.render(
            {"items": items, "title": "Новинки"},
            request,
        ),
    )


def friday_items(request):
    template = django.template.loader.get_template("catalog/item_list.html")
    items = catalog.models.Item.objects.published().filter(
        created_date__week_day=4,
    )
    return HttpResponse(
        template.render(
            {"items": items, "title": "Пятница"},
            request,
        ),
    )


def unverified_items(request):
    template = django.template.loader.get_template("catalog/item_list.html")
    items = catalog.models.Item.objects.published().filter(
        created_date=django.db.models.F("updated_date"),
    )
    return HttpResponse(
        template.render(
            {"items": items, "title": "Непроверенное"},
            request,
        ),
    )


__all__ = []
