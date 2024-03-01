import django.core.exceptions
import django.db.models
from unidecode import unidecode


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

    def __str__(self):
        return self.name[:15]

    class Meta:
        abstract = True


class CanonicalNameAbstractModel(django.db.models.Model):
    canonical_name = django.db.models.CharField(
        max_length=150,
        unique=True,
        editable=False,
        null=True,
    )

    class Meta:
        abstract = True

    def check_word(self, word, symbols, resymbols):
        new_word = word
        for i in range(len(symbols)):
            new_word = new_word.replace(symbols[i], resymbols[i])
        if (
            self._meta.model.objects.filter(canonical_name=new_word)
            .exclude(id=self.id)
            .exists()
        ):
            raise django.core.exceptions.ValidationError("Такое имя уже есть")

    def clean(self, *args, **kwargs):
        dangerous_letters = {
            "h": "н",
            "p": "р",
            "x": "х",
            "c": "s",
            "y": "u",
        }
        canon_name_main = self.name.lower()
        for i in "., ?!":
            canon_name_main = canon_name_main.replace(i, "")
        for key, value in dangerous_letters.items():
            canon_name_main = canon_name_main.replace(key, value)
        canon_name_main = unidecode(canon_name_main)

        if (
            self._meta.model.objects.filter(canonical_name=canon_name_main)
            .exclude(id=self.id)
            .exists()
        ):
            raise django.core.exceptions.ValidationError("Такое имя уже есть")

        self.canonical_name = canon_name_main


__all__ = []
