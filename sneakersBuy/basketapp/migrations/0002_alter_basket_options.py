# Generated by Django 4.2.5 on 2023-12-12 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
    ]
