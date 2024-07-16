# Generated by Django 5.0.7 on 2024-07-16 14:22

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_video_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likevideo',
            name='video_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.lesson'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='video',
            field=models.FileField(default=1, upload_to='media/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mp3', 'AVI', 'WMV', 'jpg', 'png'])]),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
