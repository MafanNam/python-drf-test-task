# Generated by Django 5.0.2 on 2024-05-02 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0004_alter_event_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="event",
            old_name="user",
            new_name="users",
        ),
    ]
