# Generated by Django 4.2 on 2024-02-20 17:15

from django.db import (
    migrations,
)


class Migration(migrations.Migration):

    dependencies = [
        (
            "catalog",
            "0003_alter_category_options_alter_item_options_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="item",
            old_name="tag",
            new_name="tags",
        ),
    ]