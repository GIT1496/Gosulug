# Generated by Django 4.2 on 2023-05-18 17:24

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_reestr_1_date_creation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reestr_2',
            name='Fam',
        ),
        migrations.RemoveField(
            model_name='reestr_2',
            name='Lastname',
        ),
        migrations.RemoveField(
            model_name='reestr_2',
            name='address_acr',
        ),
        migrations.RemoveField(
            model_name='reestr_2',
            name='name',
        ),
        migrations.AlterField(
            model_name='reestr_2',
            name='namber',
            field=models.CharField(default=core.models.func, max_length=15, verbose_name='Номер заявления'),
        ),
    ]