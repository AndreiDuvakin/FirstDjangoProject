from http import HTTPStatus

from django.test import Client, TestCase

from parameterized import parameterized


class StaticURLTests(TestCase):

    def setUp(self):
        self.client = Client()

    @parameterized.expand(
        [
            ("1",),
            ("000001",),
        ]
    )
    def test_catalog_endpoints(self, digit):
        response = self.client.get(f"/catalog/{digit}/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @parameterized.expand(
        [
            ("1",),
            ("000001",),
        ]
    )
    def test_repeat_int_endpoint(self, digit):
        response = self.client.get(f"/catalog/re/{digit}/")
        self.assertEqual(response.content.decode(), digit)

    @parameterized.expand(
        [
            ("1",),
            ("1000",),
            ("20001",),
        ]
    )
    def test_redigit_endpoint(self, digit):
        response = self.client.get(f"/catalog/converter/{digit}/")
        self.assertEqual(response.content.decode(), digit)

    @parameterized.expand(
        [
            ("0",),
            ("00213142",),
            ("ahfbd",),
        ]
    )
    def test_redigit_invalid_endpoint(self, digit):
        response = self.client.get(f"/catalog/converter/{digit}/")
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
