import django.db.models


class AbstractRootModel(django.db.models.Model):
    name = django.db.models.TextField(
        name="Название",
        help_text="Введите название",
        max_length=150,
    )
    is_published = django.db.models.BooleanField(
        name="Опубликовано",
        help_text="Статус публикации",
        default=True,
    )

    class Meta:
        abstract = True
