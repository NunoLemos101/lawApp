# Generated by Django 3.2.6 on 2022-02-16 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0028_alter_device_first_time_install'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalnote',
            name='device',
        ),
        migrations.AddField(
            model_name='personalnote',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
