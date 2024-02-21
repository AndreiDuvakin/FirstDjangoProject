import django.core.validators
import django.db.models

import core.models


def text_validator(value: str):
    if "превосходно" not in value.lower() and "роскошно" not in value.lower():
        raise django.core.validators.ValidationError(
            "Значение должно содержать слово превосходно или роскошно",
        )


class Item(core.models.AbstractRootModel):
    text = django.db.models.TextField(
        verbose_name="Текст",
        help_text="Введите описание товара",
        validators=[text_validator],
    )
    category = django.db.models.ForeignKey(
        "category",
        help_text="Выберите категорию для товара",
        on_delete=django.db.models.CASCADE,
    )
    tags = django.db.models.ManyToManyField(
        "tag",
        help_text="Выберите метки для товара",
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"


class Tag(core.models.AbstractRootModel, core.models.AbstractSlug):
    pass

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"


class Category(core.models.AbstractRootModel, core.models.AbstractSlug):
    weight = django.db.models.IntegerField(
        verbose_name="Вес",
        help_text="Введите вес категории",
        default=100,
        validators=[
            django.core.validators.MaxValueValidator(100),
            django.core.validators.MinValueValidator(1),
        ],
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
