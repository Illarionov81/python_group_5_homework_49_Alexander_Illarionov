from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user: User = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
                                      verbose_name='Пользователь')
    git_hub = models.URLField(null=True, blank=True, verbose_name='Git Hub')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    about_me = models.TextField(max_length=300, null=True, blank=True, verbose_name='О себе')

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

