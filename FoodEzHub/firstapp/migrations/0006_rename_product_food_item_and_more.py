# Generated by Django 5.0.1 on 2024-02-28 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_rename_address_customer_address_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Food_item',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='food_item',
            old_name='restaurant_id',
            new_name='restaurant',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='cart_id',
            new_name='cart',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='customer_id',
            new_name='customer',
        ),
    ]