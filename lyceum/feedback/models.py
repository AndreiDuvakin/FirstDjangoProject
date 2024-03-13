from django.contrib.auth.models import User
import django.db.models


class Feedback(django.db.models.Model):
    STATUS_CHOICES = [
        ("received", "Получено"),
        ("processing", "В обработке"),
        ("answered", "Ответ дан"),
    ]

    sender_name = django.db.models.TextField(null=True)
    text = django.db.models.TextField()
    created_on = django.db.models.DateTimeField(
        auto_now_add=True,
        null=True,
    )
    mail = django.db.models.EmailField()
    status = django.db.models.CharField(
        verbose_name="Статус обработки",
        choices=STATUS_CHOICES,
        default="received",
        max_length=20,
    )

    class Meta:
        verbose_name = "обратная связь"


class StatusLog(django.db.models.Model):
    feedback = django.db.models.ForeignKey(
        Feedback,
        on_delete=django.db.models.CASCADE,
        related_name="status_logs",
        verbose_name="Обратная связь",
    )
    user = django.db.models.ForeignKey(
        User,
        on_delete=django.db.models.CASCADE,
        related_name="status_logs",
        verbose_name="Пользователь",
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
