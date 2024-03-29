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
    if request.user.is_authenticated:
        user_profile = request.user.profile
        user_profile.coffee_count += 1
        user_profile.save()

    resp = HttpResponse()
    resp.status_code = 418
    resp.content = "Я чайник"
    return resp


def echo(request):
    if request.method == "GET":
        template = django.template.loader.get_template("homepage/echo.html")
        form = homepage.forms.EchoForm()
        return HttpResponse(template.render({"form": form}, request))

    return HttpResponseNotAllowed(["GET"])


def echo_submit(request):
    if request.method == "POST":
        text = request.POST.get("text", "")
        return HttpResponse(text, status=200)

    return HttpResponseNotAllowed(["POST"], status=405)


__all__ = []
