import django.db.models
from django.http import HttpResponse, HttpResponseNotAllowed
import django.template.loader

import catalog.models
import homepage.forms


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


def echo(request):
    template = django.template.loader.get_template("homepage/echo.html")
    form = homepage.forms.EchoForm()
    return HttpResponse(template.render({"form": form}, request))


def echo_submit(request):
    if request.method == "POST":
        text = request.POST.get("text")
        return HttpResponse(text)

    return HttpResponseNotAllowed(["POST"])


__all__ = []
