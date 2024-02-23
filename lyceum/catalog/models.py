import django.core.exceptions
import django.core.validators
import django.db.models

import catalog.validators
import core.models


class Item(core.models.AbstractRootModel):
    text = django.db.models.TextField(
        verbose_name="текст",
        help_text="Введите описание товара",
        validators=[
            catalog.validators.ValidateMustContain("роскошно", "превосходно"),
        ],
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


class Tag(
    core.models.AbstractRootModel,
    core.models.CanonicalNameAbstractModel,
):
    slug = django.db.models.SlugField(
        verbose_name="слаг",
        help_text="Введите уникальный набор букв и цифр",
        max_length=200,
    )

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"


class Category(
    core.models.AbstractRootModel,
    core.models.CanonicalNameAbstractModel,
):
    weight = django.db.models.IntegerField(
        verbose_name="вес",
        help_text="Введите вес категории",
        default=100,
        validators=[
            django.core.validators.MaxValueValidator(100),
            django.core.validators.MinValueValidator(1),
        ],
    )
    slug = django.db.models.SlugField(
        verbose_name="слаг",
        help_text="Введите уникальный набор букв и цифр",
        max_length=200,
    )
    canonical_name = django.db.models.CharField(
        max_length=150,
        unique=True,
        editable=False,
        null=True,
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
