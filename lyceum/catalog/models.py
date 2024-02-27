import django.core.exceptions
import django.core.validators
import django.db.models
import django.utils.html
from sorl.thumbnail import get_thumbnail

import catalog.validators
import core.models


class ItemMainImages(django.db.models.Model):
    main_image = django.db.models.FileField(
        "Будет приведено к 1280px", upload_to="uploads",
    )

    def get_image_x1280(self):
        return get_thumbnail(self.main_image, "1280", quality=51)

    def image_tmb(self):
        if self.main_image:
            return django.utils.html.mark_safe(
                f'<img scr="{self.main_image.url}" width=50px>',
            )
        return "Нет изображения"

    image_tmb.short_description = "превью"
    image_tmb.allow_tag = True

    list_display = ["image_tmb"]

    class Meta:
        db_table = "item_main_images"
        verbose_name = "главное изображение"
        verbose_name_plural = "главные изображения"


class ItemImages(django.db.models.Model):
    image = django.db.models.FileField(upload_to="uploads")

    class Meta:
        db_table = "item_images"
        verbose_name = "изображение товара"
        verbose_name_plural = "изображения товаров"


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
    main_image = django.db.models.OneToOneField(
        to=ItemMainImages,
        help_text="Основное изображение",
        on_delete=django.db.models.CASCADE,
        null=True,
    )
    images = django.db.models.ManyToManyField(
        ItemImages,
        help_text="Изображения товара",
        null=True,
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
            django.core.validators.MaxValueValidator(32767),
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
