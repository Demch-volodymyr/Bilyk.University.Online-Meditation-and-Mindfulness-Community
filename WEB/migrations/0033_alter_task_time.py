# Generated by Django 5.0.3 on 2024-04-02 15:40

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('WEB', '0032_alter_task_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.TimeField(default=datetime.time(15, 40, 9, 333114)),
        ),
    ]
