from ckeditor.fields import RichTextField
import django.core.exceptions
import django.core.validators
import django.db.models
import django.utils.html
from sorl.thumbnail import get_thumbnail

import catalog.validators
import core.models


class ItemManager(django.db.models.Manager):
    def on_main(self):
        return (
            self.get_queryset()
            .filter(
                is_on_main=True,
                is_published=True,
                category__is_published=True,
            )
            .select_related("category", "itemmainimages")
            .prefetch_related(
                django.db.models.Prefetch(
                    "tags",
                    queryset=catalog.models.Tag.objects.filter(
                        is_published=True,
                    ).only("name"),
                ),
            )
            .only(
                "id",
                "name",
                "text",
                "category__name",
                "itemmainimages__image",
            )
            .order_by("name")
        )

    def published(self):
        return (
            self.get_queryset()
            .filter(is_published=True, category__is_published=True)
            .select_related("category", "itemmainimages")
            .prefetch_related(
                django.db.models.Prefetch(
                    "tags",
                    queryset=catalog.models.Tag.objects.filter(
                        is_published=True,
                    ).only("name"),
                ),
            )
            .only(
                "id",
                "name",
                "text",
                "category__name",
                "itemmainimages__image",
            )
            .order_by("category__name")
        )


class Item(core.models.AbstractRootModel):
    objects = ItemManager()

    text = RichTextField(
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
        related_name="items",
    )
    is_on_main = django.db.models.BooleanField(
        verbose_name="Отобразить на главной",
        default=False,
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"


class ItemImages(django.db.models.Model):
    image = django.db.models.ImageField(upload_to="media", null=True)
    item = django.db.models.ForeignKey(
        Item,
        on_delete=django.db.models.CASCADE,
        related_name="images",
        null=True,
        blank=True,
    )

    def get_image_x300(self):
        return get_thumbnail(
            self.image,
            "300x300",
            quality=51,
            crop="center",
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
        db_table = "item_images"
        verbose_name = "изображение товара"
        verbose_name_plural = "изображения товара"


class ItemMainImages(django.db.models.Model):
    image = django.db.models.FileField(
        "Главное изображение",
        upload_to="media",
        null=True,
    )
    item = django.db.models.OneToOneField(
        to=Item,
        help_text="Основное изображение",
        on_delete=django.db.models.CASCADE,
        null=True,
        blank=True,
    )

    def get_image_400x300(self):
        return get_thumbnail(self.image, "400x300", crop="center", quality=51)

    def image_tmb(self):
        if self.image:
            return django.utils.html.mark_safe(
                f'<img src="{self.image.url}"'
                f' width=50px alt="Ошибка загрузки">',
            )
        return "Нет изображения"

    image_tmb.short_description = "превью"
    image_tmb.allow_tags = True

    class Meta:
        db_table = "item_main_images"
        verbose_name = "главное изображение"
        verbose_name_plural = "главные изображения"


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

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


__all__ = []
