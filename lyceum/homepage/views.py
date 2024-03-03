import django.db.models
from django.http import HttpResponse
import django.template.loader

import catalog.models


def home(request):
    template = django.template.loader.get_template("homepage/homepage.html")
    items = catalog.models.Item.objects.on_main()
    return HttpResponse(
        template.render(
            {
                "items": items,
            },
            request,
        ),
    )


def coffee(request):
    resp = HttpResponse()
    resp.status_code = 418
    resp.content = "Я чайник"
    return resp


__all__ = []
