# Generated by Django 3.2.6 on 2021-08-20 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0014_article_category_supercategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='brand',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='device',
            name='model',
            field=models.CharField(max_length=100),
        ),
    ]