# Generated by Django 3.2.6 on 2021-09-29 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0017_rename_paypal_comissions_transaction_paypal_commissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='folder',
        ),
        migrations.DeleteModel(
            name='Folder',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]