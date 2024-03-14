# Generated by Django 5.0.3 on 2024-03-14 18:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("logs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Logs",
            fields=[
                ("time_of_serving", models.DateTimeField(auto_now_add=True)),
                (
                    "serving_type",
                    models.CharField(
                        choices=[("fiber", "Fiber"), ("fat", "Fat")], max_length=30
                    ),
                ),
                ("log_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Progress",
            fields=[
                ("fiber_actual", models.DecimalField(decimal_places=2, max_digits=10)),
                ("fat_actual", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateTimeField()),
                ("progress_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "log",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="logs.logs"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]