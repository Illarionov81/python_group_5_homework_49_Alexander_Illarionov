# Generated by Django 2.2 on 2020-09-10 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0045_auto_20200910_1227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': [('change_users', 'Может редактировать пользователей в проекте')], 'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
    ]