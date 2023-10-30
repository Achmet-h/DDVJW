# Generated by Django 4.2.6 on 2023-10-23 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Content",
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
                ("title", models.CharField(max_length=250)),
                ("slug", models.SlugField(max_length=250)),
                ("description", models.TextField()),
                ("publish", models.DateTimeField(auto_now_add=True)),
                ("isPremium", models.BooleanField()),
                (
                    "contentType",
                    models.CharField(
                        choices=[
                            ("article", "article"),
                            ("podcast", "podcast"),
                            ("blog", "blog"),
                        ],
                        max_length=254,
                    ),
                ),
            ],
        ),
    ]