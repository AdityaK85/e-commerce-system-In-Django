# Generated by Django 3.2 on 2023-04-01 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrendNow', '0015_rename_created_at_cart_created_d_t'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_d_t',
            field=models.DateTimeField(),
        ),
    ]
