# Generated by Django 3.2.5 on 2021-07-27 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20210727_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='environments',
            field=models.ManyToManyField(to='projects.Environment'),
        ),
    ]
