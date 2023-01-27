from django.db import models
from transliterate import slugify


class Items(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    description_1 = models.CharField(max_length=100, verbose_name='Описание 1')
    description_2 = models.CharField(max_length=100, verbose_name='Описание 2')
    description_3 = models.CharField(max_length=100, verbose_name='Описание 3')
    description_4 = models.CharField(max_length=100, verbose_name='Описание 4')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} {self.price} {self.description_1} {self.description_2} {self.description_3} {self.description_4}'


class Blog(models.Model):
    STATUS_ACTIVE = 'True'
    STATUS_INACTIVE = 'False'
    STATUSES = (
        (STATUS_ACTIVE, 'положительный'),
        (STATUS_INACTIVE, 'отрицательный')
    )

    id = models.AutoField(primary_key=True, verbose_name='id')
    heading = models.CharField(max_length=250, verbose_name='Заголовк')
    slug = models.CharField(max_length=250, unique=True, verbose_name='slug')
    content = models.CharField(max_length=250, verbose_name='Содержимое')
    image = models.FileField(verbose_name='Изображение', null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUSES, default=STATUS_ACTIVE, max_length=15)
    view = models.IntegerField(verbose_name='Просмотры', default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.heading))
        super(Blog, self).save(*args, **kwargs)