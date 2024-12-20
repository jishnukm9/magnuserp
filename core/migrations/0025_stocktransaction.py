# Generated by Django 4.2.2 on 2024-04-09 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_service_pattern'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_quantity', models.IntegerField()),
                ('purchase_rate', models.FloatField()),
                ('sale_rate', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('transaction_value', models.FloatField()),
                ('transactiontype', models.CharField(max_length=50)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stock_transaction', to='core.branch')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stock_transaction', to='core.products')),
                ('purchase_tax', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stock_transaction_purchase', to='core.tax')),
                ('sale_tax', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stock_transaction_sale', to='core.tax')),
            ],
        ),
    ]
