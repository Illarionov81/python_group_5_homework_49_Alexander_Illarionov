# Generated by Django 2.2 on 2020-08-15 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0037_auto_20200815_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(default='Task', max_length=300, verbose_name='Тип'),
        ),
    ]