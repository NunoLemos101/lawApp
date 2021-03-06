# Generated by Django 3.2.6 on 2021-10-10 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0019_deviceaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportTicketMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('device', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.device')),
            ],
        ),
        migrations.CreateModel(
            name='SupportTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('state', models.CharField(choices=[('Enviado', 'Enviado'), ('Respondido', 'Respondido'), ('Fechado', 'Fechado')], max_length=10)),
                ('types', models.CharField(choices=[('BUG_REPORT', 'Reportar um Bug na aplicação'), ('CONTENT_REPORT', 'Reportar um erro no conteúdo de Direito'), ('CONTENT_SUGGESTION', 'Sugerir algo que gostavas de ver na aplicação')], max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='notes.device')),
            ],
        ),
    ]
