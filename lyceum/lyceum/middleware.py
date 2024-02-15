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
                response.content = response.content.decode()[::-1].encode()
            self.count += 1
        return response
