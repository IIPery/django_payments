# Generated by Django 5.1.6 on 2025-03-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='наименование')),
                ('percent', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='процент налога')),
            ],
            options={
                'verbose_name': 'налог',
                'verbose_name_plural': 'налоги',
                'ordering': ('-id',),
            },
        ),
    ]
