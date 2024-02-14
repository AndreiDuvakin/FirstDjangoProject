from django.http import HttpResponse


def item_list(request):
    return HttpResponse("<body>Список элементов</body>")


def item_detail(request, item_id):
    return HttpResponse("<body>Подробно элемент</body>")


def repeat_int(request, number):
    return HttpResponse(number)


def redigit(request, digit):
    return HttpResponse(digit)
