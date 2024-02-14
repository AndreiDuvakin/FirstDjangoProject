import random

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_list_endpoint(self):
        response = Client().get("/catalog/")
        self.assertEquals(response.status_code, 200)

    def test_catalog_detail_endpoint(self):
        digit = random.randint(1, 100)
        response = Client().get(f"/catalog/{str(digit)}/")
        self.assertEquals(response.status_code, 200)

    def test_repeat_int_endpoint(self):
        digit = str(random.randint(1, 100))
        response = Client().get(f"/catalog/re/{digit}/")
        self.assertEquals(response.content.decode(), digit)

    def test_redigit_endpoint(self):
        digit = str(random.randint(1, 100))
        response = Client().get(f"/catalog/re/{digit}/")
        self.assertEquals(response.content.decode(), digit)
