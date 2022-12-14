# Generated by Django 4.1.3 on 2022-11-29 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Product_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, upload_to='photos/users')),
                ('registered_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата созщдания')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата созщдания')),
                ('photo', models.ImageField(blank=True, upload_to='photos/product/%Y/%m/%d/')),
                ('views', models.IntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='comps.category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='comps.user')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='comps.product_status')),
            ],
        ),
    ]
