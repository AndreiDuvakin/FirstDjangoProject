from http import HTTPStatus

from django.conf import settings
from django.test import Client, TestCase


class StaticURLTests(TestCase):

    def test_homepage_endpoint(self):
        response = Client().get("/")
        self.assertEquals(response.status_code, 200)

    def test_coffee_endpoint(self):
        response = Client().get("/coffee/")
        self.assertEquals(
            (response.status_code, response.content.decode()),
            (HTTPStatus.IM_A_TEAPOT.value, "Я чайник"),
        )

    def test_on_flip(self):
        settings.ALLOW_REVERSE = True
        client = Client()
        responses = []
        for i in range(20):
            responses.append(client.get("/coffee/").content.decode())
        self.assertIn("кинйач Я", responses)

    def test_off_flip(self):
        settings.ALLOW_REVERSE = False
        client = Client()
        responses = []
        for i in range(20):
            responses.append(client.get("/coffee/").content.decode())
        self.assertNotIn("кинйач Я", responses)
