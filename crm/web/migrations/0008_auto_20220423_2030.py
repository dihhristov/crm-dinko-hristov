# Generated by Django 3.2.12 on 2022-04-23 17:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20220421_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contracts',
            name='price',
            field=models.CharField(max_length=7, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
        migrations.AlterField(
            model_name='offers',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.customers'),
        ),
    ]
