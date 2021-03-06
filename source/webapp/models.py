from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, ProhibitNullCharactersValidator
from django.utils import timezone

from webapp.validators import is_title, is_null

STATUS_CHOICES = [('New', 'Новая'), ('In_progress', 'В процессе'),  ('Done', 'Сделано')]
Type_CHOICES = [('Task', 'Задача'), ('Bug', 'Ошибка'),  ('Enhancement', 'Улучшение')]


class Project(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, default='None', verbose_name='Название')
    description = models.TextField(max_length=300, null=False, blank=False, default="None", verbose_name='Описание')
    starts_date = models.DateField(null=False, blank=False, verbose_name='дата начала')
    finish_date = models.DateField(null=True, blank=True, verbose_name='дата окончания')
    is_deleted = models.BooleanField(null=False, default=False)
    users = models.ManyToManyField(get_user_model(), related_name='project',
                                   verbose_name='users')

    def __str__(self):
        return "{}. {}".format(self.pk, self.name)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        permissions = [
            ('change_users', 'Может редактировать пользователей в проекте')
        ]


class IssueTracker(models.Model):
    project = models.ForeignKey('webapp.Project', related_name='issue', on_delete=models.PROTECT, verbose_name='Проект')
    summary = models.CharField(max_length=300, null=False, blank=False, default="None", verbose_name='Задание',
                               validators=[is_title, ])
    description = models.TextField(max_length=3500, null=True, blank=True, default="None description",
                                   verbose_name='Описание',
                                   validators=[is_null, ])
    status = models.ForeignKey('webapp.Status', related_name='issue', on_delete=models.PROTECT, verbose_name='Статус')
    type = models.ManyToManyField('webapp.Type', related_name='type', verbose_name='Тип')
    completion_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    users = models.ManyToManyField(get_user_model(), related_name='issue',
                                   verbose_name='users')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Status(models.Model):
    status = models.CharField(max_length=300, null=False, blank=False, choices=STATUS_CHOICES, default='New',
                              verbose_name='Статус')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Type(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False, choices=Type_CHOICES, default='Task',
                            verbose_name='Тип')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
