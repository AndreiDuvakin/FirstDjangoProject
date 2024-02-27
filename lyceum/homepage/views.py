from django.http import HttpResponse
import django.template.loader


def home(request):
    template = django.template.loader.get_template("homepage/homepage.html")
    return HttpResponse(template.render({"products": [
        {
            "id": "1",
            "name": "Корм для кошек",
            "description": "Вкусный корм для кошек"
        },
        {
            "id": "2",
            "name": "Корм для собак",
            "description": "Вкусный корм для собак"
        },
        {
            "id": "3",
            "name": "Корм для попугая",
            "description": "Вкусный корм для попугая (и голубя)"
        },
        {
            "id": "4",
            "name": "Корм для хомячков",
            "description": "Вкусный корм для хомячков (и шиншилл)"
        },
    ]}, request))


def coffee(request):
    resp = HttpResponse()
    resp.status_code = 418
    resp.content = "Я чайник"
    return resp
