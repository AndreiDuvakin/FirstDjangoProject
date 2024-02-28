from http import HTTPStatus

from django.test import Client, TestCase
import django.urls


class StaticURLTests(TestCase):
    def test_about_endpoint(self):
        url = django.urls.reverse("about:about")
        response = Client().get(url)
        self.assertEquals(response.status_code, HTTPStatus.OK)


__all__ = [StaticURLTests]
