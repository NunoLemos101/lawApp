# Generated by Django 3.2.6 on 2021-10-10 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0020_supportticket_supportticketmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportticketmessage',
            name='ticket',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='notes.supportticket'),
        ),
    ]
