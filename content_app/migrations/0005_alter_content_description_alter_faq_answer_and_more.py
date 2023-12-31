# Generated by Django 4.2.6 on 2023-11-29 09:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content_app", "0004_alter_content_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="description",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="faq",
            name="answer",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="faq",
            name="category",
            field=models.CharField(
                choices=[
                    ("Didactiek", "Didactiek"),
                    ("Begeleiding", "Begeleiding"),
                    ("Ondersteuning", "Ondersteuning"),
                ],
                max_length=254,
            ),
        ),
    ]
