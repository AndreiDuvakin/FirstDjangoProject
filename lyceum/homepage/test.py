from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get("/")
        self.assertEquals(response.status_code, 200)

    def test_coffee_endpoint(self):
        response = Client().get("/coffee")
        self.assertEquals(
            (response.status_code, response.content.decode()),
            (418, "Я чайник"),
        )
