# Generated by Django 3.2.6 on 2022-02-12 04:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0027_supportticketmessage_was_seen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='first_time_install',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
