# Generated by Django 4.1.7 on 2023-04-04 18:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrendNow', '0024_alter_cart_created_d_t_alter_cart_product_qty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_d_t',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 5, 0, 2, 42, 457391)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 5, 0, 2, 42, 457391), null=True),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='created_d_t',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 5, 0, 2, 42, 457391), null=True),
        ),
    ]
