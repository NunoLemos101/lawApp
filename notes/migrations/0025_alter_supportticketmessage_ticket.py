# Generated by Django 3.2.6 on 2021-10-11 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0024_auto_20211011_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportticketmessage',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='notes.supportticket'),
        ),
    ]
