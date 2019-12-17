from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    job_position = models.ForeignKey('JobPosition', on_delete=models.PROTECT, null=True, blank=True, related_name= "+")

    class Meta:
        verbose_name = 'Пользователь' #переводит имя User на руский в одиночном числе
        verbose_name_plural = 'Пользователи' #переводит User статей на руский в множественном числе


class JobPosition(models.Model): #базовая модель gjango
    name = models.CharField(max_length=256)
    def __str__(self):
        return f'{self.name}'
    def __str__(self):
        return f'{self.phone_number}'
        {self.viber_id}

    class Meta:
        verbose_name = 'Должность' #переводит имя JobPosition на руский в одиночном числе
        verbose_name_plural = 'Должности' #переводит JobPosition статей на руский в множественном числе
