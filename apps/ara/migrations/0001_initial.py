# Generated by Django 5.0.3 on 2024-04-16 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.CreateModel(
            name="Context",
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
                ("path", models.SlugField(blank=True)),
                (
                    "parent",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="ara.context",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ContentNode",
            fields=[
                (
                    "context_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="ara.context",
                    ),
                ),
                ("content_id", models.PositiveIntegerField()),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            bases=("ara.context",),
        ),
        migrations.CreateModel(
            name="SiteContext",
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
                (
                    "site",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="sites.site"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ContextRoot",
            fields=[
                (
                    "contentnode_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="ara.contentnode",
                    ),
                ),
                ("name", models.CharField(max_length=32, unique=True)),
            ],
            bases=("ara.contentnode",),
        ),
        migrations.AddIndex(
            model_name="context",
            index=models.Index(
                fields=["parent", "path"], name="ara_context_parent__24ec12_idx"
            ),
        ),
        migrations.AddConstraint(
            model_name="context",
            constraint=models.UniqueConstraint(
                fields=("path", "parent"),
                name="ara_context_unique_context_path",
                nulls_distinct=True,
            ),
        ),
        migrations.AddField(
            model_name="sitecontext",
            name="context_root",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ara.contextroot"
            ),
        ),
        migrations.AddField(
            model_name="contextroot",
            name="sites",
            field=models.ManyToManyField(through="ara.SiteContext", to="sites.site"),
        ),
        migrations.AddIndex(
            model_name="contentnode",
            index=models.Index(
                fields=["content_type", "content_id"],
                name="ara_content_content_10d761_idx",
            ),
        ),
    ]