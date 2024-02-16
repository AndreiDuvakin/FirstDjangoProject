from http import HTTPStatus

from django.conf import settings
from django.test import Client, TestCase

from parameterized import parameterized


class StaticURLTests(TestCase):

    def test_homepage_endpoint(self):
        response = Client().get("/")
        self.assertEquals(response.status_code, HTTPStatus.OK)

    def test_coffee_endpoint(self):
        response = Client().get("/coffee/")
        self.assertEquals(
            (response.status_code, response.content.decode()),
            (HTTPStatus.IM_A_TEAPOT.value, "Я чайник"),
        )

    @parameterized.expand([(i) for i in range(1, 21)])
    def test_on_flip(self, iteration):
        settings.ALLOW_REVERSE = True
        resp = Client().get("/coffee/").content.decode()
        self.assertIn("Я кинйач" if iteration % 10 == 0 else "Я чайник", resp)

    @parameterized.expand([(i,) for i in range(1, 21)])
    def test_off_flip(self):
        settings.ALLOW_REVERSE = False
        resp = Client().get("/coffee/").content.decode()
        self.assertIn("Я чайник", resp)
