import django.test
from django.test import TestCase
import django.urls
from parameterized import parameterized

import feedback.forms
import feedback.models


class FormTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = feedback.forms.FeedbackForm()

    @parameterized.expand(
        [
            ["text", "Текст"],
            ["mail", "Почта"],
        ],
    )
    def test_fields_name(self, field, name):
        name_label = FormTest.form.fields[field].label
        self.assertEqual(name_label, name)

    @parameterized.expand(
        [
            ["text", "Введите отзыв"],
            ["mail", "Введите свою электронную почту"],
        ],
    )
    def test_fields_help_texts(self, field, help_txt):
        help_text = FormTest.form.fields[field].help_text
        self.assertEqual(help_text, help_txt)

    @parameterized.expand(
        [
            "dsvservge",
            "esgaesfew@",
            "segFSRG@devgreb",
            "fesgewfew@csefes.",
        ],
    )
    def test_errors_in_form(self, mail):
        form_data = {"text": "some text", "mail": mail, "name": "some name"}
        response = django.test.Client().post(
            django.urls.reverse("feedback:feedback"),
            data=form_data,
            follow=True,
        )
        self.assertTrue(response.context["form"].has_error("mail"))

    def test_saving_form_data_in_db(self):
        count = feedback.models.Feedback.objects.count()
        form_data = {
            "text": "some text",
            "mail": "some@email.sm",
            "name": "some name",
        }
        django.test.Client().post(
            django.urls.reverse("feedback:feedback"),
            data=form_data,
            follow=True,
        )
        self.assertEqual(count + 1, feedback.models.Feedback.objects.count())

    def test_form_in_context(self):
        response = django.test.Client().get(
            django.urls.reverse("feedback:feedback"),
        )
        self.assertIn("form", response.context)

    def test_form_redirect(self):
        form_data = {
            "text": "some text",
            "mail": "some@email.sm",
            "name": "some name",
        }
        response = django.test.Client().post(
            django.urls.reverse("feedback:feedback"),
            data=form_data,
            follow=True,
        )
        self.assertRedirects(
            response,
            django.urls.reverse("feedback:feedback"),
        )


__all__ = []
