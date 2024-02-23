import django.core.exceptions
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

    def clean(self, *args, **kwargs):
        canon_name = self.name.lower()
        for i in "., ?!":
            canon_name = canon_name.replace(i, "")
        if (
            self._meta.model.objects.filter(canonical_name=canon_name)
            .exclude(id=self.id)
            .exists()
        ):
            raise django.core.exceptions.ValidationError("Такое имя уже есть")
        self.canonical_name = canon_name
        super().save(*args, **kwargs)
