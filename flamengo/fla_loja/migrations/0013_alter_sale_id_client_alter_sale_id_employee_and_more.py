# Generated by Django 5.1 on 2024-08-26 04:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fla_loja', '0012_remove_sale_id_shopping_remove_client_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='id_client',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='fla_loja.client'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='id_employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fla_loja.employee'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='id_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fla_loja.product'),
        ),
    ]
