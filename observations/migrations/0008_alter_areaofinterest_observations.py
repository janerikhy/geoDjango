# Generated by Django 3.2.5 on 2021-07-09 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0007_areaofinterest_observations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areaofinterest',
            name='observations',
            field=models.ManyToManyField(to='observations.ObservationTest'),
        ),
    ]
