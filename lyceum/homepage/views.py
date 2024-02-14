from django.http import HttpResponse


def home(request):
    return HttpResponse("<body>Главная</body>")


def coffee(request):
    resp = HttpResponse()
    resp.status_code = 418
    resp.content = "Я чайник"
    return resp
