from django.db import models


class News(models.Model):
    content = models.TextField()
    site = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

