# Generated by Django 5.1.6 on 2025-03-31 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_product_order_delete_productorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_order',
            name='razorpay_order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product_order',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product_order',
            name='razorpay_signature',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
