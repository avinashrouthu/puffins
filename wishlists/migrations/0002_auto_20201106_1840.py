# Generated by Django 3.1.2 on 2020-11-06 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20201102_2237'),
        ('wishlists', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userwishlist',
            name='wished_products',
        ),
        migrations.AddField(
            model_name='userwishlist',
            name='wished_products',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
