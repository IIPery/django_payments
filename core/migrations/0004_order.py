# Generated by Django 5.1.6 on 2025-03-03 19:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_tax'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('в ожидании', 'в ожидании'), ('оплачено', 'оплачено')], default='в ожидании', max_length=255, verbose_name='статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.discount', verbose_name='скидка')),
                ('items', models.ManyToManyField(blank=True, to='core.item', verbose_name='товары')),
                ('tax', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.tax', verbose_name='налог')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'ordering': ('-created_at',),
            },
        ),
    ]
