# Generated by Django 2.2 on 2020-08-12 19:50

from django.db import migrations, models
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0030_auto_20200813_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuetracker',
            name='description',
            field=models.TextField(default='None description', max_length=3500, null=True, validators=[webapp.models.is_null], verbose_name='Описание'),
        ),
    ]
