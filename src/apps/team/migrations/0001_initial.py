# Generated by Django 4.1.7 on 2023-04-08 12:50

import apps.team.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
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
                ("slug", models.SlugField(default=uuid.uuid4, unique=True)),
                ("bio", models.TextField(blank=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="static/images/team_images/team.jgp",
                        null=True,
                        upload_to="static/images/team_images/",
                    ),
                ),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "code",
                    models.CharField(
                        default=apps.team.utils.generate_code, max_length=6
                    ),
                ),
                (
                    "leader",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ("-create_at",),
            },
        ),
    ]
