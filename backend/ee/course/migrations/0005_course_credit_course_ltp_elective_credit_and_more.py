# Generated by Django 4.1 on 2023-08-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0004_elective_program"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="credit",
            field=models.FloatField(blank=True, default=1.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="course",
            name="ltp",
            field=models.CharField(default=2.5, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="elective",
            name="credit",
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="elective",
            name="ltp",
            field=models.CharField(default="1.0", max_length=10),
            preserve_default=False,
        ),
    ]