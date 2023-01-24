from django.db import models


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