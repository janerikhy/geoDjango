# Generated by Django 3.2.5 on 2021-07-19 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('max_points', models.IntegerField(default=10)),
                ('users', models.ManyToManyField(to='users.CitizenScientist')),
            ],
        ),
    ]