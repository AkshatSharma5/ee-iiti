# Generated by Django 4.1.5 on 2023-02-15 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("people", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Research",
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
                ("specialization", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=10000)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="people.people"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Projects",
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
                ("title", models.CharField(max_length=500)),
                ("funding", models.CharField(max_length=500)),
                ("duration", models.CharField(max_length=50)),
                ("project_type", models.CharField(max_length=500)),
                (
                    "worker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="people.people"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Papers",
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
                ("year", models.IntegerField()),
                ("paper", models.CharField(max_length=100)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="people.people"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Labs",
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
                ("name", models.CharField(max_length=5000)),
                ("link", models.URLField()),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="people.people"
                    ),
                ),
            ],
        ),
    ]