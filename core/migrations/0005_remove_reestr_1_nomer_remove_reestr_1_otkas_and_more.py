# Generated by Django 4.2 on 2023-04-26 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_reestr_1_vidano'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reestr_1',
            name='Nomer',
        ),
        migrations.RemoveField(
            model_name='reestr_1',
            name='Otkas',
        ),
        migrations.RemoveField(
            model_name='reestr_1',
            name='Prichina',
        ),
        migrations.RemoveField(
            model_name='reestr_1',
            name='tipogr',
        ),
        migrations.RemoveField(
            model_name='reestr_1',
            name='vidano',
        ),
    ]