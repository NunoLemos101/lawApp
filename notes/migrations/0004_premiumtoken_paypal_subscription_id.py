# Generated by Django 2.2.20 on 2021-08-15 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20210815_0321'),
    ]

    operations = [
        migrations.AddField(
            model_name='premiumtoken',
            name='paypal_subscription_id',
            field=models.CharField(blank=True, max_length=128, unique=True),
        ),
    ]
