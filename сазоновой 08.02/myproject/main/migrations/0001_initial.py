# Generated by Django 4.2.6 on 2023-12-11 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50, verbose_name='Номер')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('price', models.CharField(max_length=50, verbose_name='Цена')),
                ('quantity', models.CharField(max_length=50, verbose_name='Количество')),
                ('manufacturer', models.CharField(max_length=50, verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
