# Generated by Django 3.1.6 on 2021-04-04 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20210403_2128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='id',
            new_name='product_id',
        ),
    ]
