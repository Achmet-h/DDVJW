# Generated by Django 4.2.6 on 2023-12-04 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content_app", "0007_alter_faq_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="faq",
            name="category",
            field=models.CharField(
                choices=[
                    ("Vragen over didactiek", "Vragen over didactiek"),
                    ("Vragen over pedagogiek", "Vragen over pedagogiek"),
                    ("Algemene vragen over lesgeven", "Algemene vragen over lesgeven"),
                    ("Training en coaching", "Training en coaching"),
                ],
                max_length=254,
            ),
        ),
    ]
