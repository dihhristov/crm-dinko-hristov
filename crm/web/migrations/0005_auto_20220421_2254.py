# Generated by Django 3.2.12 on 2022-04-21 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_contracts_customer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contracts',
            name='contract_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='contracts',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.customers', verbose_name=models.CharField(max_length=100)),
        ),
    ]
