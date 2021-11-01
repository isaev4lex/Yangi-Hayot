from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок', blank=False)
    title_uz = models.CharField(max_length=200, verbose_name='Заголовок (УЗБ)', blank=False)
    title_en = models.CharField(max_length=200, verbose_name='Заголовок (АНГ)', blank=False, default='')
    img = models.ImageField(upload_to='media', verbose_name='Картинка')
    
    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'
        
    def __str__(self):
        return self.title


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
