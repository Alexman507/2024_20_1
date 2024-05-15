from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    preview = models.ImageField(upload_to='media/', **NULLABLE, verbose_name='Превью')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения')
    manufactured_at = models.DateTimeField(**NULLABLE, verbose_name='Дата производства продукта')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
