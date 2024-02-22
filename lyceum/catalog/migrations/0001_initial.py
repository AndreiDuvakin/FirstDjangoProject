# Generated by Django 4.2 on 2024-02-21 17:56

import catalog.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите название",
                        max_length=150,
                        unique=True,
                        verbose_name="название",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=True,
                        help_text="Статус публикации",
                        verbose_name="опубликовано",
                    ),
                ),
                (
                    "weight",
                    models.IntegerField(
                        default=100,
                        help_text="Введите вес категории",
                        validators=[
                            django.core.validators.MaxValueValidator(100),
                            django.core.validators.MinValueValidator(1),
                        ],
                        verbose_name="вес",
                    ),
                ),
                (
                    "slug",
                    models.TextField(
                        help_text="Введите уникальный набор букв и цифр",
                        max_length=200,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Значение должно содержать только цифры, буквы латиницы и символы - и _",
                                regex="^[a-zA-Z0-9_-]+$",
                            )
                        ],
                        verbose_name="слаг",
                    ),
                ),
            ],
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "категории",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите название",
                        max_length=150,
                        unique=True,
                        verbose_name="название",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=True,
                        help_text="Статус публикации",
                        verbose_name="опубликовано",
                    ),
                ),
                (
                    "slug",
                    models.TextField(
                        help_text="Введите уникальный набор букв и цифр",
                        max_length=200,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Значение должно содержать только цифры, буквы латиницы и символы - и _",
                                regex="^[a-zA-Z0-9_-]+$",
                            )
                        ],
                        verbose_name="слаг",
                    ),
                ),
            ],
            options={
                "verbose_name": "тег",
                "verbose_name_plural": "теги",
            },
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите название",
                        max_length=150,
                        unique=True,
                        verbose_name="название",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=True,
                        help_text="Статус публикации",
                        verbose_name="опубликовано",
                    ),
                ),
                (
                    "text",
                    models.TextField(
                        help_text="Введите описание товара",
                        validators=[
                            catalog.validators.ValidateMustContain(
                                "роскошно", "превосходно"
                            )
                        ],
                        verbose_name="текст",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        help_text="Выберите категорию для товара",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.category",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        help_text="Выберите метки для товара",
                        to="catalog.tag",
                    ),
                ),
            ],
            options={
                "verbose_name": "товар",
                "verbose_name_plural": "товары",
            },
        ),
    ]
