# Generated by Django 4.2 on 2024-02-21 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_rename_tag_item_tags"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "категории",
            },
        ),
        migrations.AlterModelOptions(
            name="item",
            options={"verbose_name": "товар", "verbose_name_plural": "товары"},
        ),
        migrations.AlterModelOptions(
            name="tag",
            options={"verbose_name": "тег", "verbose_name_plural": "теги"},
        ),
    ]