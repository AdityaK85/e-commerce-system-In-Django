# Generated by Django 3.2 on 2023-04-01 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrendNow', '0017_auto_20230401_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_d_t',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
