# Generated by Django 5.1 on 2023-10-09 17:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mbme", "0003_alter_user_options_alter_user_table"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
        migrations.AlterModelTable(
            name="user",
            table=None,
        ),
    ]