# Generated by Django 3.2 on 2023-04-01 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrendNow', '0020_alter_cart_created_d_t'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_d_t',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 1, 17, 26, 15, 382020)),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product_qty',
            field=models.IntegerField(verbose_name='Quatity'),
        ),
    ]
