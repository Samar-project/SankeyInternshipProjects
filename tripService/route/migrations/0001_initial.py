# Generated by Django 4.2.10 on 2024-02-28 19:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route_id', models.CharField(max_length=15, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{8,15}$', message='Enter a min 8 digit.')])),
                ('user_id', models.CharField(max_length=15, unique=True)),
                ('route_name', models.CharField(max_length=255)),
                ('route_origin', models.CharField(max_length=255)),
                ('route_destination', models.CharField(max_length=255)),
                ('stops', models.JSONField()),
            ],
        ),
    ]
