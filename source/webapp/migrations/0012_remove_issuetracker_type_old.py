# Generated by Django 2.2 on 2020-08-09 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20200809_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuetracker',
            name='type_old',
        ),
    ]