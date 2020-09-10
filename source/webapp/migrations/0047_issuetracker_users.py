# Generated by Django 2.2 on 2020-09-10 08:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0046_auto_20200910_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuetracker',
            name='users',
            field=models.ManyToManyField(related_name='issue', to=settings.AUTH_USER_MODEL, verbose_name='users'),
        ),
    ]