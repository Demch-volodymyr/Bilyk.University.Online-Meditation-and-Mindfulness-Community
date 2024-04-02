# Generated by Django 5.0.3 on 2024-04-02 15:40

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Forum', '0002_post_parent_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='parent_post',
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses',
                                                  to='Forum.post')),
            ],
        ),
    ]
