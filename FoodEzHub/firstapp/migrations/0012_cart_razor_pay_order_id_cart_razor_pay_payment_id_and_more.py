# Generated by Django 5.0.1 on 2024-03-29 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0011_alter_order_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='razor_pay_order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='razor_pay_payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='razor_pay_payment_signature',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
