import django.db.models


class Feedback(django.db.models.Model):
    text = django.db.models.TextField()
    created_on = django.db.models.DateTimeField(
        auto_now_add=True,
        null=True,
    )
    mail = django.db.models.EmailField()

    class Meta:
        verbose_name = "обратная связь"


__all__ = []
