# Generated by Django 4.2.2 on 2024-04-28 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_customerbookingrepair_bookingid'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerbookingrepair',
            name='branch',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customer_booking', to='core.branch'),
        ),
    ]
