# Generated by Django 4.2 on 2023-06-10 10:19

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('SANZ_1', '0013_remove_lic1_inn_remove_lic1_ogrn_remove_lic1_ur_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lic1',
            name='vid',
            field=models.CharField(choices=[('Деятельность в области использования возбудителей инфекционных заболеваний человека и животных ', 'Деятельность в области использования возбудителей инфекционных заболеваний человека и животных'), ('Деятельность в области использования источников ионизирующего излучения (генерирующих)', 'Деятельность в области использования источников ионизирующего излучения (генерирующих)')], default='Деятельность в области использования возбудителей инфекционных заболеваний человека и животных', max_length=500, verbose_name='Вид деятельности'),
        ),
        migrations.AlterField(
            model_name='sez1',
            name='sootv',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('СанПиН 1.2.3685-21 "Гигиенические нормативы и требования к обеспечению безопасности и (или) безвредности для человека факторов среды обитания"', 'СанПиН 1.2.3685-21 "Гигиенические нормативы и требования к обеспечению безопасности и (или) безвредности для человека факторов среды обитания"'), ('СанПиН 2.3/2.4.3590-20 "Санитарно-эпидемиологические требования к организации общественного питания населения"', 'СанПиН 2.3/2.4.3590-20 "Санитарно-эпидемиологические требования к организации общественного питания населения"')], max_length=500, null=True, verbose_name='Соответствует: '),
        ),
        migrations.AlterField(
            model_name='sez1',
            name='vidano',
            field=models.CharField(blank=True, default='Управление Роспотребнадзора по Архангельской области', max_length=150, verbose_name='Кем выдано'),
        ),
    ]
