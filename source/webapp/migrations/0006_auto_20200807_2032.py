# Generated by Django 2.2 on 2020-08-07 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20200806_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuetracker',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='issue', to='webapp.Status', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='issuetracker',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type', to='webapp.Type', verbose_name='Тип'),
        ),
    ]