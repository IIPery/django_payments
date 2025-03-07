# Generated by Django 5.1.6 on 2025-03-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='наименование')),
                ('percent', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='процент скидки')),
            ],
            options={
                'verbose_name': 'скидка',
                'verbose_name_plural': 'скидки',
                'ordering': ('-id',),
            },
        ),
    ]
