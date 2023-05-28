# Generated by Django 4.2 on 2023-05-14 18:03

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_reestr_1_namber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reestr_1',
            name='date_creation',
            field=models.DateTimeField(verbose_name='Дата регистрации заявления'),
        ),
        migrations.AlterField(
            model_name='reestr_1',
            name='date_rendering',
            field=models.DateField(verbose_name='Дата оказания государственной услуги'),
        ),
        migrations.AlterField(
            model_name='reestr_1',
            name='namber',
            field=models.CharField(default=core.models.func, max_length=15, verbose_name='Номер заявления'),
        ),
        migrations.AlterField(
            model_name='reestr_1',
            name='vid',
            field=models.CharField(choices=[('Проект', 'Проект'), ('Производство', 'Производство'), ('Лицензия', 'Лицензия'), ('Санитарно-защитная зона', 'Санитарно-защитная зона'), ('Свидетельство о государственной регистрации', 'Свидетельство о государственной регистрации')], default='Проект', max_length=50, verbose_name='Вид деятельности'),
        ),
    ]