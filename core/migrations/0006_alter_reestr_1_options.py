# Generated by Django 4.2 on 2023-04-27 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_reestr_1_nomer_remove_reestr_1_otkas_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reestr_1',
            options={'ordering': ['namber'], 'verbose_name': 'Заявление на получение санитарно-эпидемиологического заключения, лицензии, свидетельства о государственной регистрации продукции', 'verbose_name_plural': 'заявления на получение санитарно-эпидемиологического заключения, лицензии, свидетельства о государственной регистрации продукции'},
        ),
    ]
