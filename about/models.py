from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', blank=False)
    surname = models.CharField(max_length=100, verbose_name='Фамилия', blank=False)
    work = models.CharField(max_length=100, verbose_name='Должность', blank=False)

    name_lat = models.CharField(max_length=100, verbose_name='Имя (на Латинице)', blank=False)
    surname_lat = models.CharField(max_length=100, verbose_name='Фамилия (на Латинице)', blank=False)
    work_lat = models.CharField(max_length=100, verbose_name='Должность (на Латинице)', blank=False)

    img = models.ImageField(upload_to='media', verbose_name='Фото', blank=False)

    class Meta:
        verbose_name = 'Человека'
        verbose_name_plural = 'Команда'

    def __str__(self):
        return self.name


class Banner(models.Model):
    banner = models.ImageField(upload_to='media', blank=False)

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

    def __str__(self):
        return 'Баннер'


class MetaTags(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title', blank=False)
    title_uz = models.CharField(max_length=300, verbose_name='Title (УЗБ)', blank=False)
    title_en = models.CharField(max_length=300, verbose_name='Title (АНГ)', blank=False)
    keywords = models.TextField(verbose_name='Keywords (Через запятую/Предложением)', blank=False)
    description = models.TextField(verbose_name='Description', blank=False)

    class Meta:
        verbose_name = 'Мета тег'
        verbose_name_plural = 'Мета теги'

    def __str__(self):
        return self.title
