# Generated by Django 3.2.20 on 2024-07-29 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0063_branchstock_created_date_brand_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coasubaccounts',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
