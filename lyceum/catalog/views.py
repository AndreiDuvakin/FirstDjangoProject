from collections import defaultdict

from django.http import HttpResponse
import django.shortcuts
import django.template.loader

import catalog.models


def item_list(request):
    template = django.template.loader.get_template("catalog/item_list.html")
    items = catalog.models.Item.objects.published()
    items_by_category = defaultdict(list)
    for item in items:
        items_by_category[item.category.name].append(item)
    return HttpResponse(
        template.render(
            {
                "items_by_category": items_by_category.items(),
            },
            request,
        ),
    )


def item_detail(request, item_id):
    template = django.template.loader.get_template("catalog/item.html")
    item = django.shortcuts.get_object_or_404(
        catalog.models.Item.objects.published(),
        pk=item_id,
    )
    return HttpResponse(template.render({"item": item}, request))


def repeat_int(request, number):
    return HttpResponse(number)


def redigit(request, digit):
    return HttpResponse(digit)


__all__ = []
