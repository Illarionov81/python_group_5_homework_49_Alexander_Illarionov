# Generated by Django 2.2 on 2020-08-12 19:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_auto_20200813_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuetracker',
            name='description',
            field=models.TextField(blank=True, default='None description', max_length=3500, null=True, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.ProhibitNullCharactersValidator], verbose_name='Описание'),
        ),
    ]
