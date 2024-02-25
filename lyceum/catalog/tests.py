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
            name="хорошие",
            slug="f34vraevr7veu4",
            canonical_name="horoshie",
        )
        cls.tag = catalog.models.Tag.objects.create(
            is_published=True,
            name="новое",
            slug="bf3c63gc773gvw543i7v",
            canonical_name="novoe",
        )

    @parameterized.expand(
        [
            ("SomeName", "превосходнороскошно"),
            ("NameSome", "превосходное роскошное"),
            ("omnomnomName", ""),
        ],
    )
    def test_create_invalide_item(self, name, text):
        item_count = catalog.models.Item.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.item = catalog.models.Item(
                name=name,
                is_published=True,
                text=text,
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(ModelsTests.tag)

        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_count,
        )

    @parameterized.expand(
        [
            ("SomeName", "превосходно роскошно"),
            ("NameSome", "превосходно роскошное"),
            ("omnomnomName", "роскошно"),
        ],
    )
    def test_create_valide_item(self, name, text):
        item_count = catalog.models.Item.objects.count()
        self.item = catalog.models.Item(
            name=name,
            is_published=True,
            text=text,
            category=ModelsTests.category,
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(ModelsTests.tag)
        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_count + 1,
        )

    @parameterized.expand(
        [
            ("Хор!ошие",),
            ("хOрOш!ие",),
            ("хор!ошие",),
        ],
    )
    def test_invalidate_category(self, name):
        cat_count = catalog.models.Category.objects.count()
        print(catalog.models.Category.objects.first().canonical_name, 1)
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.cat = catalog.models.Category(
                name=name,
                slug="f34vrab3fgu",
            )
            self.cat.full_clean()
            self.cat.save()
            print(catalog.models.Category.objects.last().canonical_name, 2)
        self.assertEqual(cat_count, catalog.models.Category.objects.count())

    @parameterized.expand(
        [
            "Somename1234",
            "s.omena!me91",
            "    s.omena   !me91",
            "s.omena!medsavdc1",
        ],
    )
    def test_validate_category(self, name):
        cat_count = catalog.models.Category.objects.count()
        self.cat = catalog.models.Category(
            name=name,
            slug="f34vrab3fgu",
        )
        self.cat.full_clean()
        self.cat.save()
        self.assertEqual(
            cat_count + 1,
            catalog.models.Category.objects.count(),
        )

    @parameterized.expand(
        [
            "no!vo.e",
            "nов ое",
            "Ново.е",
        ],
    )
    def test_invalidate_tag(self, name):
        tag_count = catalog.models.Tag.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.tg = catalog.models.Tag(
                name=name,
                slug="jgbwee234",
            )
            self.tg.full_clean()
            self.tg.save()
        self.assertEqual(tag_count, catalog.models.Tag.objects.count())

    @parameterized.expand(
        [
            "Somename1234",
            "s.omena!me91",
            "    s.omena   !me91",
            "s.omena!medsavdc1",
        ],
    )
    def test_validate_tag(self, name):
        tag_count = catalog.models.Tag.objects.count()
        self.tg = catalog.models.Tag(
            name=name,
            slug="jgbwee234",
        )
        self.tg.full_clean()
        self.tg.save()
        self.assertEqual(tag_count + 1, catalog.models.Tag.objects.count())
