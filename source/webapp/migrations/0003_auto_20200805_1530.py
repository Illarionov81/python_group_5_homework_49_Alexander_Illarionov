# Generated by Django 2.2 on 2020-08-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200805_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(choices=[('Task', 'Задача'), ('Bug', 'Ошибка'), ('Enhancement', 'Улучшение')], default='Task', max_length=300, verbose_name='Тип'),
        ),
    ]
