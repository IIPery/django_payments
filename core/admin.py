from django.contrib import admin

from core import models


@admin.register(models.Item)
class Item(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name', 'description', 'price')


@admin.register(models.Discount)
class Discount(admin.ModelAdmin):
    list_display = ('name', 'percent')
    search_fields = ('name', 'percent')


@admin.register(models.Tax)
class Tax(admin.ModelAdmin):
    list_display = ('name', 'percent')
    search_fields = ('name', 'percent')


@admin.register(models.Order)
class Order(admin.ModelAdmin):
    list_display = ('id','status', 'get_total_price')
    search_fields = ('id','status', 'get_total_price')

    @admin.display(description='общая сумма')
    def get_total_price(self,obj):
        return obj.get_total_price()
