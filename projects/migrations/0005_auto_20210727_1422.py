# Generated by Django 3.2.5 on 2021-07-27 12:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects/images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='video',
            field=models.FileField(upload_to='projects/videos', validators=[django.core.validators.FileExtensionValidator(['MOV', 'mp4', 'avi', 'mov', 'MP4'], 'The file format is not accepted')]),
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='Describe the reward')),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.sponsor')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='organizers',
            field=models.ManyToManyField(to='projects.Organization'),
        ),
        migrations.AddField(
            model_name='project',
            name='rewards',
            field=models.ManyToManyField(to='projects.Reward'),
        ),
    ]
