# Generated by Django 5.1 on 2023-10-11 00:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog_v1", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="PostComment",
        ),
    ]