# Generated by Django 3.2 on 2023-04-01 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrendNow', '0021_auto_20230401_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_d_t',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 1, 18, 49, 40, 249367)),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product_qty',
            field=models.IntegerField(blank=True, default='1', null=True, verbose_name='Quatity'),
        ),
    ]