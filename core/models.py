from django.db import models


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


