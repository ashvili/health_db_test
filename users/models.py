from django.contrib.auth.models import AbstractUser
from django.db import models


class AsdUser(AbstractUser):
    data_lang = models.IntegerField(null=True)
    ui_lang = models.IntegerField(null=True)
    def group_name(self):
        try:
            return self.groups.all().first().name
        except:
            return ''

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
