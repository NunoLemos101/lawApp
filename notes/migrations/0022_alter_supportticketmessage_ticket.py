# Generated by Django 3.2.6 on 2021-10-10 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0021_supportticketmessage_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportticketmessage',
            name='ticket',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='notes.supportticket'),
        ),
    ]
