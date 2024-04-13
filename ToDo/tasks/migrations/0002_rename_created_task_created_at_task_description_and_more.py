# Generated by Django 5.0.4 on 2024-04-13 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="created",
            new_name="created_at",
        ),
        migrations.AddField(
            model_name="task",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="task",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]