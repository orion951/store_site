# Generated by Django 4.1.3 on 2022-11-30 08:17

import base.services
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='ФИО')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('registered_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата созщдания')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=base.services.get_path_upload_avatar, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg']), base.services.validate_size_image])),
            ],
        ),
    ]
