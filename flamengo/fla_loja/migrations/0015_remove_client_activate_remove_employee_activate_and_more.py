# Generated by Django 5.1 on 2024-08-26 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fla_loja', '0014_client_activate_employee_activate_product_activate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='activate',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='activate',
        ),
        migrations.RemoveField(
            model_name='product',
            name='activate',
        ),
    ]
