# Generated by Django 3.0.3 on 2020-03-28 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200328_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='customer',
            name='number',
            field=models.CharField(max_length=20),
        ),
    ]
