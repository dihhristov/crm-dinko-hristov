# Generated by Django 3.2.12 on 2022-04-21 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_contracts_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='contracts',
            name='customer_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]