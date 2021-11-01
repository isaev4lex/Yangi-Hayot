from django.db import models
from .ru_to_eng import translate
from django.urls import reverse


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок', blank=False)
    description = models.TextField(verbose_name='Описание', blank=False)
    title_uz = models.CharField(max_length=200, verbose_name='Заголовок (УЗБ)', blank=False)
    description_uz = models.TextField(verbose_name='Описание (УЗБ)', blank=False)
    title_en = models.CharField(max_length=200, verbose_name='Заголовок (АНГ)', blank=False)
    description_en = models.TextField(verbose_name='Описание (АНГ)', blank=False)
    slug = models.CharField(max_length=200, verbose_name='URL (необязательно)', blank=True, unique=True)
    img = models.ImageField(upload_to='media', verbose_name='Картинка')

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title

    def get_url_ru(self):
        return reverse("card", args=[self.slug])

    def get_url_uz(self):
        return reverse("card", args=[self.slug, 'uz'])

    def get_url_en(self):
        return reverse("card", args=[self.slug, 'en'])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translate(self.title)
        super().save(*args, **kwargs)


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
