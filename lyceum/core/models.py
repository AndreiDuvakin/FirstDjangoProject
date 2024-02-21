import django.core.validators
import django.db.models


class AbstractRootModel(django.db.models.Model):
    name = django.db.models.TextField(
        "Название",
        help_text="Введите название",
        max_length=150,
    )
    is_published = django.db.models.BooleanField(
        "Опубликовано",
        help_text="Статус публикации",
        default=True,
    )

    class Meta:
        abstract = True


class AbstractSlug(django.db.models.Model):
    slug = django.db.models.TextField(
        name="Слаг",
        help_text="Введите уникальный набор букв и цифр",
        max_length=200,
        unique=True,
        validators=[
            django.core.validators.RegexValidator(
                regex=r"^[a-zA-Z0-9_-]+$",
                message="Значение должно содержать только цифры, "
                "буквы латиницы и символы - и _",
            ),
        ],
    )

    class Meta:
        abstract = True
