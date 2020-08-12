# Generated by Django 2.2 on 2020-08-12 18:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_auto_20200813_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuetracker',
            name='description',
            field=models.TextField(blank=True, default='None description', max_length=3500, null=True, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='issuetracker',
            name='summary',
            field=models.CharField(default='None description', max_length=300, verbose_name='Задание'),
        ),
    ]
