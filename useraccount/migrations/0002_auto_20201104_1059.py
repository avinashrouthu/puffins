# Generated by Django 3.1.2 on 2020-11-04 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='default_postcode',
            new_name='default_zipcode',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='default_county',
        ),
    ]
