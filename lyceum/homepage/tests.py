from http import HTTPStatus

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
