# Generated by Django 3.2.5 on 2021-07-21 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210720_1131'),
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challange',
            name='users',
            field=models.ManyToManyField(blank=True, to='users.CitizenScientist'),
        ),
    ]
