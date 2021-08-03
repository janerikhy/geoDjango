# Generated by Django 3.2.5 on 2021-07-21 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('challenges', '0001_initial'),
        ('observations', '0009_alter_observationtest_options'),
        ('users', '0002_auto_20210720_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latin_name', models.CharField(max_length=250)),
                ('scientific_name', models.CharField(blank=True, max_length=250, null=True)),
                ('common_name', models.CharField(max_length=250)),
                ('taxon_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='projects/imgs')),
                ('video', models.FileField(upload_to='projects/videos')),
                ('areas', models.ManyToManyField(to='observations.AreaOfInterest')),
                ('challenges', models.ManyToManyField(to='challenges.Challange')),
                ('creators', models.ManyToManyField(to='users.Scientist')),
                ('participants', models.ManyToManyField(to='users.CitizenScientist')),
                ('species', models.ManyToManyField(to='projects.Species')),
            ],
        ),
    ]
