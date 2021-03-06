# Generated by Django 2.2 on 2020-08-22 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0041_auto_20200822_1707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AddField(
            model_name='issuetracker',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='issue', to='webapp.Project', verbose_name='Проект'),
            preserve_default=False,
        ),
    ]
