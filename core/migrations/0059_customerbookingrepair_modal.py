# Generated by Django 4.2.8 on 2024-07-18 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0058_phonebrand_arabic_name_phonemodal_arabic_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerbookingrepair',
            name='modal',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
