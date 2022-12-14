# Generated by Django 4.1.3 on 2022-11-30 08:21

import base.services
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=base.services.get_path_upload_avatar, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg']), base.services.validate_size_image], verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='country',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='registered_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации'),
        ),
    ]
