import django.db.models


class AbstractRootModel(django.db.models.Model):
    name = django.db.models.CharField(
        verbose_name="название",
        help_text="Введите название",
        max_length=150,
        unique=True,
    )
    is_published = django.db.models.BooleanField(
        verbose_name="опубликовано",
        help_text="Статус публикации",
        default=True,
    )

    class Meta:
        abstract = True
