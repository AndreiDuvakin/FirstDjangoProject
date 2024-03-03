from django.http import HttpResponse
import django.shortcuts
import django.template.loader

import catalog.models


def item_list(request):
    template = django.template.loader.get_template("catalog/item_list.html")
    items = catalog.models.Item.objects.published()
    return HttpResponse(
        template.render(
            {
                "items": items,
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
    for i in item.images.all():
        print(i.image)
    return HttpResponse(template.render({"item": item}, request))


def repeat_int(request, number):
    return HttpResponse(number)


def redigit(request, digit):
    return HttpResponse(digit)


__all__ = []
