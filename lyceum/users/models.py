import time

import django.conf
import django.core.exceptions
import django.core.validators
import django.db.models
from sorl.thumbnail import get_thumbnail


class Profile(django.db.models.Model):

    def get_upload_path(self, filename):
        return f"users/avatars/{self.user_id}/{time.time()}_{filename}"

    user = django.db.models.OneToOneField(
        django.conf.settings.AUTH_USER_MODEL,
        verbose_name="пользователь",
        related_name="profile",
        related_query_name="profile",
        on_delete=django.db.models.CASCADE,
    )
    birthday = django.db.models.DateField(
        null=True,
        blank=True,
    )
    image = django.db.models.ImageField(
        null=True,
        blank=True,
        verbose_name="аватар пользователя",
        upload_to=get_upload_path,
    )
    coffee_count = django.db.models.PositiveIntegerField(
        "количество переходов по /coffee/",
        default=0,
    )

    def get_image_x300(self):
        return get_thumbnail(
            self.image,
            "300x300",
            quality=51,
            crop="center",
        )

    def download_images(self):
        return django.utils.html.mark_safe(
            f'<a href="/download/{self.image}" '
            f"download>Скачать изображение</a>",
        )

    def image_tmb(self):
        if self.image:
            return django.utils.html.mark_safe(
                f'<img scr="{self.image.url}" width=50px>',
            )

        return "Нет изображения"

    image_tmb.short_description = "превью"
    image_tmb.allow_tags = True

    list_display = ["image_tmb"]

    class Meta:
        verbose_name = "данные пользователя"
        verbose_name_plural = "данные пользователей"


__all__ = []
