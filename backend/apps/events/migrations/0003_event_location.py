# Generated by Django 5.0.2 on 2024-05-03 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="location",
            field=models.CharField(blank=True, default="Kiev, Ukraine", max_length=255, verbose_name="location"),
        ),
    ]
