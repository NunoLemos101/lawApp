# Generated by Django 3.2.6 on 2021-08-18 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brute_income', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('liquid_income', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('paypal_comissions', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]
