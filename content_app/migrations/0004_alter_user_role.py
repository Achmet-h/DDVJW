# Generated by Django 4.2.6 on 2023-10-19 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content_app", "0003_alter_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("trainer", "trainer"), ("client", "client")],
                default="client",
                max_length=255,
            ),
        ),
    ]
