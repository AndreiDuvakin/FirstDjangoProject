from http import HTTPStatus

import django.core.exceptions
import django.test
from django.test import Client, TestCase
from parameterized import parameterized

import catalog.models


class StaticURLTests(TestCase):

    def setUp(self):
        self.client = Client()

    @parameterized.expand(
        [
            ("1",),
            ("12",),
            ("100",),
        ],
    )
    def test_catalog_endpoints(self, digit):
        response = self.client.get(f"/catalog/{digit}/")
        self.assertEqual(
            response.status_code,
            HTTPStatus.OK,
        )

    @parameterized.expand(
        [
            ("1",),
            ("12",),
            ("100",),
        ],
    )
    def test_repeat_int_endpoint(self, digit):
        response = self.client.get(f"/catalog/re/{digit}/")
        self.assertEqual(
            response.content.decode(),
            digit,
        )

    @parameterized.expand(
        [
            ("1",),
            ("1000",),
            ("20001",),
        ],
    )
    def test_redigit_endpoint(self, digit):
        response = self.client.get(f"/catalog/converter/{digit}/")
        self.assertEqual(
            response.content.decode(),
            digit,
        )

    @parameterized.expand(
        [
            ("0",),
            ("00213142",),
            ("ahfbd",),
        ],
    )
    def test_redigit_invalid_endpoint(self, digit):
        response = self.client.get(f"/catalog/converter/{digit}/")
        self.assertEqual(
            response.status_code,
            HTTPStatus.NOT_FOUND,
        )


class ModelsTests(django.test.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.category = catalog.models.Category.objects.create(
            is_published=True,
            name="SomeName",
            slug="f34vraevr7veu4",
        )
        cls.tag = catalog.models.Tag.objects.create(
            is_published=True,
            name="SomeName",
            slug="bf3c63gc773gvw543i7v",
        )

    def test_create_invalide_item(self):
        item_count = catalog.models.Item.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.item = catalog.models.Item(
                name="SomeName",
                is_published=True,
                text="SomeText",
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(ModelsTests.tag)

        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_count,
        )

    def test_create_valide_item(self):
        item_count = catalog.models.Item.objects.count()
        self.item = catalog.models.Item(
            name="SomeName",
            is_published=True,
            text="превосходнороскошно",
            category=ModelsTests.category,
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(ModelsTests.tag)
        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_count + 1,
        )

    def test_invalidate_category(self):
        cat_count = catalog.models.Category.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.cat = catalog.models.Category(
                "SomeName",
                slug="f34vrab3fgu",
            )
            self.cat.full_clean()
            self.cat.save()
        self.assertEqual(cat_count, catalog.models.Category.objects.count())

    def test_validate_category(self):
        cat_count = catalog.models.Category.objects.count()
        self.cat = catalog.models.Category(
            name="SomeName234",
            slug="f34vrab3fgu",
        )
        self.cat.full_clean()
        self.cat.save()
        self.assertEqual(
            cat_count + 1,
            catalog.models.Category.objects.count(),
        )

    def test_invalidate_tag(self):
        tag_count = catalog.models.Tag.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.tg = catalog.models.Category(
                name="SomeName",
                slug="jgbwee234",
            )
            self.tg.full_clean()
            self.tg.save()
        self.assertEqual(tag_count, catalog.models.Tag.objects.count())

    def test_validate_tag(self):
        tag_count = catalog.models.Tag.objects.count()
        self.tg = catalog.models.Tag(
            name="SomeName234",
            slug="jgbwee234",
        )
        self.tg.full_clean()
        self.tg.save()
        self.assertEqual(tag_count + 1, catalog.models.Tag.objects.count())
