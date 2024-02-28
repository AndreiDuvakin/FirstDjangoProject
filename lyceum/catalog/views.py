from django.http import HttpResponse
import django.template.loader


def item_list(request):
    template = django.template.loader.get_template("catalog/item_list.html")
    return HttpResponse(
        template.render(
            {
                "products": [
                    {
                        "id": "1",
                        "name": "Корм для кошек",
                        "description": "Вкусный корм для кошек",
                    },
                    {
                        "id": "2",
                        "name": "Корм для собак",
                        "description": "Вкусный корм для собак",
                    },
                    {
                        "id": "3",
                        "name": "Корм для попугая",
                        "description": "Вкусный корм для попугая (и голубя)",
                    },
                    {
                        "id": "4",
                        "name": "Корм для хомячков",
                        "description": "Вкусный корм для хомячков (и шиншилл)",
                    },
                ],
            },
            request,
        ),
    )


def item_detail(request, item_id):
    template = django.template.loader.get_template("catalog/item.html")
    return HttpResponse(template.render({"item_id": item_id}, request))


def repeat_int(request, number):
    return HttpResponse(number)


def redigit(request, digit):
    return HttpResponse(digit)


__all__ = [
    item_list,
    repeat_int,
    redigit,
]
