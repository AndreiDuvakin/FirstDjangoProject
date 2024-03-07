from http import HTTPStatus

from django.conf import settings
from django.test import Client, TestCase
import django.urls


class StaticURLTests(TestCase):

    def test_homepage_endpoint(self):
        url = django.urls.reverse("homepage:homepage")
        response = Client().get(url)
        self.assertEquals(response.status_code, HTTPStatus.OK)

    def test_coffee_endpoint(self):
        url = django.urls.reverse("homepage:coffee")
        response = Client().get(url)
        self.assertEquals(
            (response.status_code, response.content.decode()),
            (HTTPStatus.IM_A_TEAPOT.value, "Я чайник"),
        )

    def test_on_flip(self):
        url = django.urls.reverse("homepage:coffee")
        settings.ALLOW_REVERSE = True
        responses = []
        for iteration in range(1, 20):
            responses.append(Client().get(url).content.decode())
        self.assertIn("Я кинйач", responses)

    def test_off_flip(self):
        url = django.urls.reverse("homepage:coffee")
        settings.ALLOW_REVERSE = False
        responses = []
        for iteration in range(1, 20):
            responses.append(Client().get(url).content.decode())
        self.assertNotIn("Я кинйач", responses)


__all__ = []
