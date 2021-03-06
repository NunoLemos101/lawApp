# Generated by Django 3.2.6 on 2021-08-18 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_alter_afterpaymenttoken_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='afterpaymenttoken',
            name='before_payment_token',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.beforepaymenttoken'),
        ),
        migrations.AddField(
            model_name='beforepaymenttoken',
            name='is_subscribed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='beforepaymenttoken',
            name='payment_was_received',
            field=models.BooleanField(default=False),
        ),
    ]
