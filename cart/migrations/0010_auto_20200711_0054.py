# Generated by Django 3.0 on 2020-07-11 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200709_0441'),
        ('cart', '0009_item_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='storage', to='products.Estoque'),
        ),
    ]
