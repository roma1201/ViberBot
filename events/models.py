from django.db import models
from django.conf import settings

class Event(models.Model):
    name = models.CharField(max_length=256)
    data = models.DateTimeField()

    class Meta:
        verbose_name = 'Мероприятия' #переводит имя статьи на руский в одиночном числе
        verbose_name_plural = 'Мероприятии' #переводит имя статей на руский в множественном числе


class Ticket(models.Model):
    data = models.DateTimeField(auto_now=True)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Билет' #переводит имя статьи на руский в одиночном числе
        verbose_name_plural = 'Билеты' #переводит имя статей на руский в множественном числе