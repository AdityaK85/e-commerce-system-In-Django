# Generated by Django 3.2 on 2023-03-14 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrendNow', '0010_rename_allproduct_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='catergory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TrendNow.category'),
        ),
    ]
