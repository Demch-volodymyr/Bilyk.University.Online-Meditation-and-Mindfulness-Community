# Generated by Django 5.0.3 on 2024-03-12 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WEB', '0003_profile_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='google_id',
            new_name='profile_id',
        ),
    ]