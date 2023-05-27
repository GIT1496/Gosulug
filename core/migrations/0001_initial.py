# Generated by Django 4.2 on 2023-04-23 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reestr_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namber', models.CharField(max_length=15, verbose_name='Номер заявления')),
                ('date_creation', models.DateField(verbose_name='Дата регистрации заявления')),
                ('date_rendering', models.DateField(verbose_name='Дата оказания государственной услуги')),
                ('predpr', models.CharField(max_length=200, verbose_name='Предприятие')),
                ('vid', models.CharField(choices=[('Проект', 'Проект'), ('Производство', 'Производство'), ('Лицензия', 'Лицензия'), ('Санитарно-защитная зона', 'Санитарно-защитная зона'), ('Свидетельство о государственной регистрации', 'Свидетельство о государственной регистрации')], max_length=50, verbose_name='Вид деятельности')),
                ('dejat', models.CharField(max_length=200, verbose_name='Наименование деятельности')),
                ('fact_adr', models.CharField(max_length=200, verbose_name='Фактический адрес осуществления деятельности')),
                ('adres_Applicant', models.CharField(max_length=200, verbose_name='Юридический адрес заявителя, представителя заявителя')),
                ('Otd', models.CharField(choices=[('Гигиена детей и подростков', 'Гигиена детей и подростков'), ('Гигиена труда', 'Гигиена труда'), ('Эпид. отдел', 'Эпид. отдел'), ('Отдел санитарно-эпидемиологических заключений', 'Отдел санитарно-эпидемиологических заключений')], max_length=120, verbose_name='Отдел исполнитель')),
                ('sp', models.CharField(choices=[('ПГУ', 'ПГУ'), ('Нарочным', 'Нарочным'), ('Почта', 'Почта')], max_length=200, verbose_name='Способ направления документов')),
                ('Otkas', models.CharField(choices=[('Отказ в оказании государственной  услуги', 'Отказ в оказании государственной  услуги'), ('Оказание государственной услуги', 'Оказание государственной услуги')], max_length=50, verbose_name='Статус государственной услуги')),
                ('Prichina', models.CharField(blank=True, max_length=200, verbose_name='Причина отказа')),
                ('Nomer', models.CharField(blank=True, max_length=60, verbose_name='Номер санитарно-эпидемиологического заключения, лицензии, свидетельства о государственной регистрации продукции')),
                ('tipogr', models.CharField(blank=True, max_length=50, verbose_name='Типографский номер бланка')),
                ('Vip', models.BooleanField(verbose_name='Выполнено')),
                ('Prim', models.CharField(blank=True, max_length=200, verbose_name='Примечание')),
            ],
            options={
                'verbose_name': 'заявление на получение санитарно-эпидемиологического заключения, лицензии, свидетельства о государственной регистрации продукции',
                'verbose_name_plural': 'заявления на получение санитарно-эпидемиологического заключения, лицензии, свидетельства о государственной регистрации продукции',
                'ordering': ['namber'],
            },
        ),
        migrations.CreateModel(
            name='Reestr_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namber', models.CharField(max_length=15, verbose_name='Номер заявления')),
                ('date_creation', models.DateField(verbose_name='Дата регистрации заявления')),
                ('date_rendering', models.DateField(verbose_name='Дата оказания государственной услуги')),
                ('fact_adr', models.CharField(max_length=200, verbose_name='Фактический адрес объекта')),
                ('cl', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=2, verbose_name='Класс опасности')),
                ('Type_application', models.CharField(choices=[('Установление санитарно-защитной зоны', 'Установление санитарно-защитной зоны'), ('Изменение санитарно-защитной зоны', 'Изменение санитарно-защитной зоны'), ('Сокращение санитарно-защитной зоны', 'Сокращение санитарно-защитной зоны')], max_length=100, verbose_name='Тип объекта')),
                ('Object', models.CharField(choices=[('Действующий', 'Действующий'), ('Проектируемый', 'Проектируемый'), ('Реконструированный', 'Реконструированный')], max_length=50, verbose_name='Тип объекта')),
                ('Applicant', models.CharField(max_length=200, verbose_name='Наименование заявителя, представителя заявителя')),
                ('adres_Applicant', models.CharField(max_length=200, verbose_name='Юридический адрес заявителя, представителя заявителя')),
                ('Fam', models.CharField(max_length=100, verbose_name='Фамилия руководителя организации')),
                ('name', models.CharField(max_length=50, verbose_name='Имя руководителя организации')),
                ('Lastname', models.CharField(max_length=50, verbose_name='Отчество руководителя организации')),
                ('Accredited_organization', models.CharField(blank=True, max_length=200, verbose_name='Аккредитованная организация, проводившая исследования')),
                ('Accreditation_number', models.CharField(blank=True, max_length=50, verbose_name='Номер аттестата аккредитации')),
                ('address_acr', models.CharField(max_length=25, verbose_name='Юридический адрес аккредитованной организации')),
                ('Name_obj', models.CharField(max_length=200, verbose_name='Наименование проекта')),
                ('designer', models.CharField(max_length=200, verbose_name='Наименование проектировщика')),
                ('adr', models.CharField(max_length=200, verbose_name='Юридический адрес проектировщика')),
                ('conclusion_number', models.CharField(max_length=150, verbose_name='Номер экспертного заключения')),
                ('accreditation', models.CharField(max_length=200, verbose_name='Номер аттестата аккредитации экспертной организации')),
                ('name_acr', models.CharField(max_length=200, verbose_name='Кем выдано экспертное заключение')),
                ('adr1', models.CharField(max_length=200, verbose_name='Юридический адрес экспертной организации')),
                ('SEZ1', models.CharField(blank=True, max_length=26, verbose_name='Номер санитарно-эпидемиологического заключения')),
                ('SEZ2', models.CharField(choices=[('Роспотребнадзор', 'Роспотребнадзор'), ('Иная организация', 'Иная организация')], max_length=40, verbose_name='Кем выдано')),
            ],
            options={
                'verbose_name': 'заявление на выдачу решения об установлении санитарно-защитной зоны',
                'verbose_name_plural': 'заявления на выдачу решения об установлении санитарно-защитной зоны',
                'ordering': ['namber'],
            },
        ),
    ]
