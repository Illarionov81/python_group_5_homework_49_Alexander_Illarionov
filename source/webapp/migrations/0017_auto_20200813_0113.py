# Generated by Django 2.2 on 2020-08-12 19:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_auto_20200813_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuetracker',
            name='description',
            field=models.TextField(blank=True, default='None description', max_length=3500, null=True, validators=[django.core.validators.ProhibitNullCharactersValidator()], verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='issuetracker',
            name='summary',
            field=models.CharField(default='None description', max_length=300, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Задание'),
        ),
    ]
