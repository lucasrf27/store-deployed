# Generated by Django 3.0 on 2020-07-01 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_produto_activate'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='mensagem',
            field=models.TextField(default='Mensagem', max_length=600),
        ),
    ]
