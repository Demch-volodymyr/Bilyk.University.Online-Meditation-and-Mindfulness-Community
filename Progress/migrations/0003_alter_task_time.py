# Generated by Django 5.0.3 on 2024-04-06 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Progress', '0002_alter_task_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.TimeField(default=datetime.time(15, 3, 41, 684607)),
        ),
    ]
