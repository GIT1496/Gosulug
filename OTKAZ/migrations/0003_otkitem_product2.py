# Generated by Django 4.2 on 2023-05-21 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_reestr2summary_alter_reestr_2_type_application'),
        ('OTKAZ', '0002_otkazsummary_alter_otk_date_creation'),
    ]

    operations = [
        migrations.AddField(
            model_name='otkitem',
            name='product2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_items2', to='core.reestr_2', verbose_name='Заявление2'),
        ),
    ]
