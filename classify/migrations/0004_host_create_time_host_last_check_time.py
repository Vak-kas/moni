# Generated by Django 5.0.6 on 2024-06-15 09:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classify', '0003_host_remove_wordcount_classification_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='host',
            name='last_check_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
