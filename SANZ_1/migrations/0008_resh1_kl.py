# Generated by Django 4.2 on 2023-06-03 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SANZ_1', '0007_alter_resh1_options_resh1_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='resh1',
            name='kl',
            field=models.CharField(blank=True, max_length=2, verbose_name='Класс опасности объекта'),
        ),
    ]