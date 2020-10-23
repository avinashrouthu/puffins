# Generated by Django 3.1.2 on 2020-10-23 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='date_of_dispatch',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='material_1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='material_2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
