# Generated by Django 5.0.1 on 2024-03-30 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0013_remove_feedback_food_item_cart_restaurant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='restaurant',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.restaurant'),
        ),
    ]
