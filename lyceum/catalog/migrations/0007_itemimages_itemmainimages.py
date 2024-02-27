# Generated by Django 4.2 on 2024-02-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_alter_category_weight"),
    ]

    operations = [
        migrations.CreateModel(
            name="ItemImages",
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
                ("image", models.FileField(upload_to="uploads")),
            ],
            options={
                "verbose_name": "изображение товара",
                "verbose_name_plural": "изображения товаров",
            },
        ),
        migrations.CreateModel(
            name="ItemMainImages",
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
                ("main_image", models.FileField(upload_to="uploads")),
            ],
            options={
                "verbose_name": "главное изображение",
                "verbose_name_plural": "главные изображения",
            },
        ),
    ]
