from django.http import HttpResponse
import django.template.loader


def description(request):
    template = django.template.loader.get_template("about/about.html")
    return HttpResponse(template.render({}, request))


__all__ = []
