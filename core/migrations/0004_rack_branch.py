# Generated by Django 4.2.2 on 2024-02-21 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_expensecategory_branch_expensetype_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='rack',
            name='branch',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rack_nos', to='core.branch'),
        ),
    ]