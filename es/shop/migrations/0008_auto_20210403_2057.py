# Generated by Django 3.1.6 on 2021-04-03 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_delete_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
                ('query', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_id',
            new_name='id',
        ),
    ]
