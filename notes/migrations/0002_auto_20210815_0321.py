# Generated by Django 2.2.20 on 2021-08-15 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='public_unique_id',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='unique_id',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
