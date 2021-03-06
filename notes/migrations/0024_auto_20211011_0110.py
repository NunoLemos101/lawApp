# Generated by Django 3.2.6 on 2021-10-11 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0023_rename_types_supportticket_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportticket',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.device'),
        ),
        migrations.AlterField(
            model_name='supportticketmessage',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.device'),
        ),
        migrations.AlterField(
            model_name='supportticketmessage',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.supportticket'),
        ),
    ]
