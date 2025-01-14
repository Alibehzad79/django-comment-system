# Generated by Django 5.0.6 on 2024-06-06 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog_app", "0001_initial"),
        ("comments_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="article",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="blog_app.article",
                verbose_name="Article",
            ),
            preserve_default=False,
        ),
    ]
