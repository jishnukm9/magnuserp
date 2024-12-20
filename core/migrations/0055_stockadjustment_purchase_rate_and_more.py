# Generated by Django 4.2.8 on 2024-07-15 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_stockadjustment_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockadjustment',
            name='purchase_rate',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='stockadjustment',
            name='purchase_tax',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='stockadjustment',
            name='sale_rate',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='stockadjustment',
            name='sale_tax',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
