# Generated by Django 4.2.6 on 2023-10-19 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("content_app", "0006_user"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]
