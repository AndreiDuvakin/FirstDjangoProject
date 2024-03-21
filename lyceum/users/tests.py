import datetime
import unittest.mock

import django.contrib.auth
import django.core.mail
import django.test
import django.urls
import django.utils


class TestUserViews(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = django.test.Client()
        cls.user_model = django.contrib.auth.get_user_model()
        cls.user = cls.user_model.objects.create_user(
            email="test@example.com",
            password="testpassword",
            username="testuserr",
        )

    @classmethod
    def tearDownClass(cls):
        cls.user_model.objects.all().delete()

        super().tearDownClass()

    def test_signup(self):
        data = {
            "username": "testinguser",
            "email": "testuser@example.com",
            "password1": "testpassword",
            "password2": "testpassword",
        }

        response = self.client.post(
            django.urls.reverse("users:signup"),
            data,
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            django.urls.reverse("users:login"),
        )

        self.assertTrue(
            self.user_model.objects.filter(username="testinguser").exists(),
        )

        user = django.shortcuts.get_object_or_404(
            django.contrib.auth.get_user_model().objects,
            username="testinguser",
        )

        self.assertTrue(
            user.is_authenticated,
        )

    @django.test.override_settings(DEFAULT_USER_IS_ACTIVE=False)
    def test_user_activation_positive(self):
        self.client.post(
            django.urls.reverse("users:signup"),
            data={
                "username": "test_username",
                "password1": "testpassword",
                "password2": "testpassword",
            },
        )
        user = django.shortcuts.get_object_or_404(
            django.contrib.auth.get_user_model().objects,
            username="test_username",
        )
        self.assertFalse(user.is_active)
        self.client.get(
            django.urls.reverse("users:activate", args=["test_username"]),
        )
        user = django.shortcuts.get_object_or_404(
            django.contrib.auth.get_user_model().objects,
            username="test_username",
        )
        self.assertTrue(user.is_active)

    @django.test.override_settings(DEFAULT_USER_IS_ACTIVE=False)
    def test_user_activation_negative(self):
        self.client.post(
            django.urls.reverse("users:signup"),
            data={
                "username": "test_username2",
                "password1": "testpassword",
                "password2": "testpassword",
            },
        )
        expired_dt = django.utils.timezone.now() + datetime.timedelta(hours=13)
        with unittest.mock.patch(
            "django.utils.timezone.now",
        ) as mocked_timezone:
            mocked_timezone.return_value = expired_dt
            self.client.get(
                django.urls.reverse("users:activate", args=["test_username2"]),
            )

        user = django.shortcuts.get_object_or_404(
            django.contrib.auth.get_user_model().objects,
            username="test_username2",
        )

        self.assertFalse(user.is_active)


__all__ = []
