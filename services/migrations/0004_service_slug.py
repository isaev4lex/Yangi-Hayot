# Generated by Django 3.2.7 on 2021-09-14 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_metatags_title_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='URL (необязательно)'),
        ),
    ]