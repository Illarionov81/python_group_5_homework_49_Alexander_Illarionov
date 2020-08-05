from django.db import models

STATUS_CHOICES = [('New', 'Новая'), ('In_progress', 'В процессе'),  ('Done', 'Сделано')]
Type_CHOICES = [('Task', 'Задача'), ('Bug', 'Ошибка'),  ('Enhancement', 'Улучшение')]

class IssueTracker(models.Model):
    summary = models.CharField(max_length=300, null=False, blank=False, default="None description", verbose_name='Задание')
    description = models.TextField(max_length=3500, null=True, blank=True, default="None description", verbose_name='Описание')
    status = models.ForeignKey('webapp.Status', related_name='issue', on_delete=models.PROTECT, default='New', verbose_name='Статус')
    type = models.ForeignKey('webapp.Type', related_name='type', on_delete=models.PROTECT, default='Task', verbose_name='Тип')
    completion_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return "{}. {}".format(self.pk, self.summary)

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
