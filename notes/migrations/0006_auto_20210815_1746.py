# Generated by Django 2.2.20 on 2021-08-15 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20210815_0323'),
    ]

    operations = [
        migrations.CreateModel(
            name='AfterPaymentToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BeforePaymentToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paypal_subscription_id', models.CharField(max_length=128, unique=True)),
                ('device_public_id', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='PremiumToken',
        ),
        migrations.AddField(
            model_name='device',
            name='premium_token',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.AfterPaymentToken'),
        ),
    ]
