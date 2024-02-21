import django.core.exceptions
import django.core.validators
import django.db.models
import django.utils.deconstruct

import core.models

# раньше это была функция-валидатор, но она больше не нужна
# а миграции ее сохранили и не дают удалить :(
text_validator = None  # памагити избавится от этого


@django.utils.deconstruct.deconstructible
class ValidateMustContain:
    def __init__(self, *words):
        self.words = list(map(lambda word: word.lower(), words))

    def __call__(self, value):
        value = value.lower()
        for word in self.words:
            if word not in value:
                raise django.core.exceptions.ValidationError(
                    f"Значение должно содержать слово '{word}'",
                )


class Item(core.models.AbstractRootModel):
    text = django.db.models.TextField(
        verbose_name="текст",
        help_text="Введите описание товара",
        validators=[ValidateMustContain("роскошно", "превосходно")],
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


class Tag(core.models.AbstractRootModel):
    slug = django.db.models.TextField(
        verbose_name="слаг",
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
        verbose_name = "тег"
        verbose_name_plural = "теги"


class Category(core.models.AbstractRootModel):
    weight = django.db.models.IntegerField(
        verbose_name="вес",
        help_text="Введите вес категории",
        default=100,
        validators=[
            django.core.validators.MaxValueValidator(100),
            django.core.validators.MinValueValidator(1),
        ],
    )
    slug = django.db.models.TextField(
        verbose_name="слаг",
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
        verbose_name = "категория"
        verbose_name_plural = "категории"
