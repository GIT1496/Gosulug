# Generated by Django 4.2 on 2023-05-14 17:47

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_reestr_1_date_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reestr_1',
            name='namber',
            field=models.CharField(blank=True, default=core.models.func, max_length=15, verbose_name='Номер заявления'),
        ),
    ]