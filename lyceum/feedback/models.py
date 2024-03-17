import time

import django.conf
import django.db.models


class Feedback(django.db.models.Model):
    STATUS_CHOICES = [
        ("received", "Получено"),
        ("processing", "В обработке"),
        ("answered", "Ответ дан"),
    ]

    text = django.db.models.TextField()
    created_on = django.db.models.DateTimeField(
        auto_now_add=True,
        null=True,
    )
    status = django.db.models.CharField(
        verbose_name="Статус обработки",
        choices=STATUS_CHOICES,
        default="received",
        max_length=20,
    )

    class Meta:
        verbose_name = "обратная связь"


class FeedbackAuther(django.db.models.Model):
    feedback = django.db.models.OneToOneField(
        Feedback,
        related_name="auther",
        on_delete=django.db.models.CASCADE,
    )
    name = django.db.models.TextField(
        "имя",
        max_length=50,
        null=True,
        blank=True,
    )
    mail = django.db.models.EmailField("электронная почта")


class FeedbackImages(django.db.models.Model):
    def get_upload_path(self, filename):
        return f"uploads/{self.feedback_id}/{time.time()}_{filename}"

    image = django.db.models.ImageField(
        upload_to=get_upload_path,
        null=True,
        blank=True,
    )
    feedback = django.db.models.ForeignKey(
        Feedback,
        on_delete=django.db.models.CASCADE,
        related_name="images",
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "feedback_images"
        verbose_name = "изображение отзыва"
        verbose_name_plural = "изображения отзыва"


class StatusLog(django.db.models.Model):
    feedback = django.db.models.ForeignKey(
        Feedback,
        on_delete=django.db.models.CASCADE,
        related_name="status_logs",
        verbose_name="Обратная связь",
    )
    user = django.db.models.ForeignKey(
        django.conf.settings.AUTH_USER_MODEL,
        on_delete=django.db.models.CASCADE,
    )
    timestamp = django.db.models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время изменения статуса",
    )
    _from = django.db.models.CharField(
        max_length=20,
        verbose_name="Старый статус",
        db_column="from",
    )
    to = django.db.models.CharField(
        max_length=20,
        verbose_name="Новый статус",
    )

    class Meta:
        verbose_name = "лог статуса"
        verbose_name_plural = "логи статусов"


__all__ = []
