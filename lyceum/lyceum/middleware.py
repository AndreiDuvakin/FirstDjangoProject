import re

from django.conf import settings


class FlipWordMiddleware:
    count = 0

    def __init__(self, get_response):
        self.get_response = get_response
        self.allow_flip = settings.ALLOW_REVERSE

    def __call__(self, request):
        response = self.get_response(request)
        if self.allow_flip:
            self.__class__.count += 1
            if self.__class__.count == 10:
                cont = response.content.decode()
                for m in re.finditer(r"\b[а-яА-ЯЁё]+\b", cont):
                    start, end = m.start(), m.end()
                    cont = cont[:start] + cont[start:end][::-1] + cont[end:]

                self.__class__.count = 0
                response.content = cont.encode()

            self.count += 1

        return response


__all__ = [FlipWordMiddleware]
