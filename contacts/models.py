from django.db import models


class Phone(models.Model):
    phone_number = models.CharField(max_length=23, verbose_name='Номер', blank=False)

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'

    def __str__(self):
        return self.phone_number


class Address(models.Model):
    city = models.CharField(max_length=30, verbose_name='Город (RU)', blank=False)
    street = models.CharField(max_length=30, verbose_name='Адрес (RU)', blank=False)
    landmark = models.CharField(max_length=40, verbose_name='Ориентир (RU)', blank=True)

    city_uz = models.CharField(max_length=30, verbose_name='Город (UZ)', blank=False)
    street_uz = models.CharField(max_length=30, verbose_name='Адрес (UZ)', blank=False)
    landmark_uz = models.CharField(max_length=40, verbose_name='Ориентир (UZ)', blank=True)

    city_en = models.CharField(max_length=30, verbose_name='Город (ENG)', blank=False)
    street_en = models.CharField(max_length=30, verbose_name='Адрес (ENG)', blank=False)
    landmark_en = models.CharField(max_length=40, verbose_name='Ориентир (ENG)', blank=True)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f'{self.city}, {self.street}'


class EMail(models.Model):
    email = models.CharField(max_length=23, verbose_name='Почта', blank=False)

    class Meta:
        verbose_name = 'email'
        verbose_name_plural = 'email'

    def __str__(self):
        return self.email


class SocialLink(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', blank=False)
    img = models.ImageField(upload_to='media', verbose_name='Иконка', blank=False)
    link = models.TextField(verbose_name='Ссылка', blank=False)

    class Meta:
        verbose_name = 'Соцсеть'
        verbose_name_plural = 'Соцсети'

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
