# Generated by Django 3.2.5 on 2021-07-21 11:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210721_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='video',
            field=models.FileField(upload_to='projects/videos', validators=[django.core.validators.FileExtensionValidator(['MOV', 'mp4', 'avi', 'mov', 'MP4'], 'File Upload Error')]),
        ),
    ]
