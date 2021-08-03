# Generated by Django 3.2.5 on 2021-07-29 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210720_1131'),
        ('projects', '0008_remove_project_creators'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.scientist'),
            preserve_default=False,
        ),
    ]
