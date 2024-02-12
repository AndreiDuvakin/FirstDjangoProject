from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_list_endpoint(self):
        response = Client().get("/catalog")
        self.assertEquals(response.status_code, 200)

    def test_catalog_detail_endpoint(self):
        response = Client().get("/catalog/1")
        self.assertEquals(response.status_code, 200)
