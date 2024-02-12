from django.test import TestCase, Client


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get("/")
        self.assertEquals(response.status_code, 200)
