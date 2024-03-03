from http import HTTPStatus

import django.core.exceptions
import django.test
from django.test import Client, TestCase
import django.urls
from parameterized import parameterized

import catalog.models


class StaticURLTests(TestCase):

    def setUp(self):
        self.client = Client()

    @parameterized.expand(
        [
            ("1",),
            ("2",),
            ("100",),
        ],
    )
    def test_repeat_int_endpoint(self, digit):
        url = django.urls.reverse(
            "catalog:re_number",
            kwargs={"number": digit},
        )
        response = self.client.get(url)
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
        url = django.urls.reverse("catalog:converter", kwargs={"digit": digit})
        response = self.client.get(url)
        self.assertEqual(
            response.content.decode(),
            digit,
        )

    @parameterized.expand(
        [("0",), ("00213142",), ("eanmewmf")],
    )
    def test_redigit_invalid_endpoint(self, digit):
        with self.assertRaises(django.urls.exceptions.NoReverseMatch):
            url = django.urls.reverse(
                "catalog:converter",
                kwargs={"digit": digit},
            )
            response = self.client.get(url)
            self.assertEqual(
                response.status_code,
                HTTPStatus.NOT_FOUND,
            )


class ModelsTests(django.test.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.category_pub = catalog.models.Category.objects.create(
            is_published=True,
            name="хорошие",
            slug="f34vraevr7veu4",
            canonical_name="khoroshie",
        )
        cls.tag_pub = catalog.models.Tag.objects.create(
            is_published=True,
            name="новое",
            slug="bf3c63gc773gvw543i7v",
            canonical_name="novoe",
        )
        cls.category_unpub = catalog.models.Category.objects.create(
            is_published=False,
            name="не опубликованная категория",
            slug="dagf34vraevr7veu4",
            canonical_name="ne opublikovannaya",
        )
        cls.tag_unpub = catalog.models.Tag.objects.create(
            is_published=False,
            name="не опубликованный тэг",
            slug="fsbbf3c63gc773gvw543i7v",
            canonical_name="ne opublikovanniy",
        )
        cls.item_pub = catalog.models.Item.objects.create(
            is_published=True,
            name="опубликованный товар",
            text="",
            category_id=1,
            is_on_main=True,
        )

        cls.item_pub2 = catalog.models.Item.objects.create(
            is_published=True,
            name="опубликованный товар 2",
            text="",
            category_id=1,
            is_on_main=False,
        )
        cls.item_unpub = catalog.models.Item.objects.create(
            is_published=False,
            name="не опубликованный товар",
            text="",
            category_id=1,
            is_on_main=False,
        )

    def test_home_page_correct_show_items(self):
        response = django.test.Client().get(
            django.urls.reverse("homepage:homepage"),
        )
        self.assertIn("items", response.context)

    def test_home_page_correct_count_items(self):
        response = django.test.Client().get(
            django.urls.reverse("homepage:homepage"),
        )
        items = response.context["items"]
        self.assertEqual(django.db.models.query.QuerySet, type(items))
        self.assertEqual(len(items), 1)

    def test_list_item_page_correct_show_items(self):
        response = django.test.Client().get(
            django.urls.reverse("catalog:item_list"),
        )
        self.assertIn("items", response.context)

    def test_list_item_page_correct_count_items(self):
        response = django.test.Client().get(
            django.urls.reverse("catalog:item_list"),
        )
        items = response.context["items"]
        self.assertEqual(django.db.models.query.QuerySet, type(items))
        self.assertEqual(len(items), 2)

    def test_item_page_correct_show(self):
        response = django.test.Client().get(
            django.urls.reverse("catalog:item", kwargs={"item_id": 1}),
        )
        self.assertIn("item", response.context)

    def test_item_page_not_published(self):
        response = django.test.Client().get(
            django.urls.reverse("catalog:item", kwargs={"item_id": 3}),
        )
        self.assertNotIn("item", response.context)

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
            self.item.tags.add(ModelsTests.tag_pub)

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
            category=ModelsTests.category_pub,
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(ModelsTests.tag_pub)
        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_count + 1,
        )

    @parameterized.expand(
        [
            ("х.О!рошие",),
            ("XoPоШие",),
            ("хорошие",),
        ],
    )
    def test_invalidate_category(self, name):
        cat_count = catalog.models.Category.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.cat = catalog.models.Category(
                name=name,
                slug="f34vrab3fgu",
            )
            self.cat.full_clean()
            self.cat.save()
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
            "Hов ое",
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


__all__ = []
