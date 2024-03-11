import re

from django.conf import settings


class FlipWordMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.count = 1
        self.allow_flip = settings.ALLOW_REVERSE

    def __call__(self, request):
        response = self.get_response(request)
        if self.allow_flip:
            if self.count % 10 == 0:
                cont = response.content.decode()
                clean_string = ""
                for i in cont:
                    if bool(re.match(r"^[а-яА-Я ]+$", i)):
                        clean_string += i

                current_russian_words = clean_string.split()
                for i in current_russian_words:
                    cont = cont.replace(i, i[::-1])

                response.content = cont

            self.count += 1

        return response


__all__ = [FlipWordMiddleware]
