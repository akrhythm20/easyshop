# Generated by Django 3.1.6 on 2021-04-04 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20210404_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact2',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
                ('query', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
