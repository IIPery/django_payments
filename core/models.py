from django.db import models
from core import consts


class Item(models.Model):
    name = models.CharField('наименование', max_length=255, db_index=True)
    description = models.TextField('описание', max_length=255, blank=True)
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('-id',)

    def __str__(self) -> str:
        return self.name


class Discount(models.Model):
    name = models.CharField('наименование', max_length=255, db_index=True)
    percent = models.DecimalField('процент скидки', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'скидка'
        verbose_name_plural = 'скидки'
        ordering = ('-id',)

    def __str__(self):
        return f'{self.name} - {self.percent}%'


class Tax(models.Model):
    name = models.CharField('наименование', max_length=255, db_index=True)
    percent = models.DecimalField('процент налога', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'налог'
        verbose_name_plural = 'налоги'
        ordering = ('-id',)

    def __str__(self):
        return f'{self.name} - {self.percent}%'


class Order(models.Model):
    items = models.ManyToManyField('core.Item', verbose_name='товары', blank=True)
    discount = models.ForeignKey(
        'core.Discount',
        verbose_name='скидка',
        on_delete=models.SET_NULL,
        null=True,
        blank= True
    )
    tax = models.ForeignKey(
        'core.Tax',
        verbose_name = 'налог',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    status = models.CharField(
        'статус',
        choices=consts.STATUS_CHOICES,
        default=consts.STATUS_PENDING,
        max_length=255
    )
    created_at = models.DateTimeField('дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ('-created_at',)

    def __str__(self):
        return f'Заказ №{self.id}'

    def get_total_price(self) -> float:
        total = sum(item.price for item in self.items.all())

        if self.discount:
            total -= total * (self.discount.percent / 100)
        if self.tax:
            total -= total * (self.tax.percent / 100)

        return round(total, 2)
