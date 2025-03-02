from django.contrib import admin

from core import models


@admin.register(models.Item)
class Item(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name', 'description', 'price')