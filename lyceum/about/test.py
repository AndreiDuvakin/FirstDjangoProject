from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_about_endpoint(self):
        response = Client().get("/about")
        self.assertEquals(response.status_code, 200)
