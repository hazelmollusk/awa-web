# Generated by Django 5.1 on 2024-08-28 13:31

import awa.models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware
import functools
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectLink",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "icon",
                    models.ImageField(
                        blank=True,
                        height_field="icon_height",
                        null=True,
                        upload_to=functools.partial(
                            awa.models.image_upload_to, *(), **{"role": "icons"}
                        ),
                        width_field="icon_width",
                    ),
                ),
                (
                    "icon_height",
                    models.PositiveSmallIntegerField(
                        blank=True, editable=False, null=True
                    ),
                ),
                (
                    "icon_width",
                    models.PositiveSmallIntegerField(
                        blank=True, editable=False, null=True
                    ),
                ),
                ("name", models.CharField(max_length=32)),
                ("url", models.URLField(max_length=128)),
                ("header", models.BooleanField(default=False)),
                (
                    "created_by",
                    django_currentuser.db.models.fields.CurrentUserField(
                        default=django_currentuser.middleware.get_current_authenticated_user,
                        null=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        related_name="%(app_label)s_%(class)s_created",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    django_currentuser.db.models.fields.CurrentUserField(
                        default=django_currentuser.middleware.get_current_authenticated_user,
                        null=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        on_update=True,
                        related_name="%(app_label)s_%(class)s_modified",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
