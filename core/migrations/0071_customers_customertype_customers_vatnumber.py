# Generated by Django 4.2.2 on 2024-08-19 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0070_whatsappstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='customertype',
            field=models.CharField(default=None, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customers',
            name='vatnumber',
            field=models.CharField(default=None, max_length=200, null=True, unique=True),
        ),
    ]
