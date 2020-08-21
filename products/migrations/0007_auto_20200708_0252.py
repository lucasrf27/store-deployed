# Generated by Django 3.0 on 2020-07-08 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_estoque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='tamanho',
            field=models.CharField(choices=[('Adulto', (('P', 'P'), ('M', 'M'), ('G', 'G'))), ('Infantil', (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'))), ('Calsa', (('36', '36'), ('38', '38'), ('40', '40'), ('42', '42'), ('44', '44'), ('46', '46'), ('48', '48'), ('50', '50'))), ('unknown', 'Unknown')], max_length=100),
        ),
    ]
