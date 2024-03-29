# Generated by Django 4.2 on 2024-03-02 18:15

import catalog.validators
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [
        ("catalog", "0005_alter_item_text"),
        (
            "catalog",
            "0006_rename_main_image_itemmainimages_image_and_more",
        ),
        ("catalog", "0007_alter_itemimages_options"),
        ("catalog", "0008_item_is_on_main"),
        ("catalog", "0009_alter_item_is_on_main"),
    ]

    dependencies = [
        ("catalog", "0004_alter_item_images_alter_item_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="text",
            field=ckeditor.fields.RichTextField(
                help_text="Введите описание товара",
                validators=[
                    catalog.validators.ValidateMustContain(
                        "роскошно", "превосходно"
                    )
                ],
                verbose_name="текст",
            ),
        ),
        migrations.RenameField(
            model_name="itemmainimages",
            old_name="main_image",
            new_name="image",
        ),
        migrations.RemoveField(
            model_name="item",
            name="images",
        ),
        migrations.RemoveField(
            model_name="item",
            name="main_image",
        ),
        migrations.AddField(
            model_name="itemimages",
            name="item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="catalog.item",
            ),
        ),
        migrations.AddField(
            model_name="itemmainimages",
            name="item",
            field=models.OneToOneField(
                blank=True,
                help_text="Основное изображение",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.item",
            ),
        ),
        migrations.AlterField(
            model_name="itemimages",
            name="image",
            field=models.ImageField(null=True, upload_to="media"),
        ),
        migrations.AlterModelOptions(
            name="itemimages",
            options={
                "verbose_name": "изображение товара",
                "verbose_name_plural": "изображения товара",
            },
        ),
        migrations.AddField(
            model_name="item",
            name="is_on_main",
            field=models.BooleanField(
                default=False, verbose_name="Отобразить на главную"
            ),
        ),
    ]
