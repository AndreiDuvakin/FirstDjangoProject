# Generated by Django 4.2 on 2024-03-01 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_rename_main_image_itemmainimages_image_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="itemimages",
            options={
                "verbose_name": "изображение товара",
                "verbose_name_plural": "изображения товара",
            },
        ),
    ]
