import re

import django.db.models
import transliterate

ONLY_LETTERS_REGEX = re.compile(
    r"[^a-zA-Zа-яА-Я]",
)


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

    def gen_canonical_name(self):
        try:
            transliterated = transliterate.translit(
                self.name.lower(), reversed=True,
            )
        except transliterate.exceptions.LanguageDetectionError:
            transliterated = self.name.lower()

        return ONLY_LETTERS_REGEX.sub("", transliterated)

    def clean(self, *args, **kwargs):
        self.canonical_name = self.gen_canonical_name()
