# Generated by Django 5.0.7 on 2024-07-16 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_likevideo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='name',
        ),
    ]
