# Generated by Django 5.0.6 on 2024-05-21 13:37

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_alter_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=tinymce.models.HTMLField(),
        ),
    ]