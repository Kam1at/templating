# Generated by Django 4.1.5 on 2023-01-27 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templating', '0002_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(null=True, upload_to='images/', verbose_name='Изображение'),
        ),
    ]