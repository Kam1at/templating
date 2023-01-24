# Generated by Django 4.1.5 on 2023-01-24 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('description_1', models.CharField(max_length=100, verbose_name='Описание 1')),
                ('description_2', models.CharField(max_length=100, verbose_name='Описание 2')),
                ('description_3', models.CharField(max_length=100, verbose_name='Описание 3')),
                ('description_4', models.CharField(max_length=100, verbose_name='Описание 4')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
