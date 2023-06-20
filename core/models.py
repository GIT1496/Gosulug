from django.db import models
from django.urls import reverse


# Функция для автоматического формирования номера заявления через id, добавлена в default namber
def func():
    nm = Reestr_1.objects.all()
    nm1 = 1
    for i1 in nm:
        if i1.id > nm1:
            nm1 = i1.id
    nm1 = nm1 + 1
    nn = '29-' + str(nm1) + "-2023"
    return nn

def func2():
    nm = Reestr_2.objects.all()
    nm1 = 1
    for i1 in nm:
        if i1.id > nm1:
            nm1 = i1.id
    nm1 = nm1 + 1
    nn = '29-' + str(nm1) + "-2023"
    return nn




# Модель для хранения заявлений на СЭЗ, лицензии и т.д.
class Reestr_1(models.Model):
    SPOSOB_NAPR = [('ПГУ', 'ПГУ'),
                   ('Нарочным', 'Нарочным'),
                   ('Почта', 'Почта')]
    VID = [
                              ('Проект', 'Проект'),
                              ('Производство', 'Производство'),
                              ('Лицензия', 'Лицензия'),
                              ('Санитарно-защитная зона', 'Санитарно-защитная зона'),
                              ('Свидетельство о государственной регистрации', 'Свидетельство о государственной регистрации'),
                              ('Переформление лицензии', 'Переформление лицензии'),
                              ('Переформление СЭЗ', 'Переформление СЭЗ'),
                              ('Переформление Свидетельства', 'Переформление Свидетельства'),
                          ]


    namber = models.CharField(max_length=15, null=False, default=func, verbose_name='Номер заявления')
    date_creation = models.DateTimeField(null=False, verbose_name='Дата регистрации заявления')
    date_rendering = models.DateField(null=False, verbose_name='Дата оказания государственной услуги')
    predpr = models.CharField(max_length=200, blank=False, verbose_name='Предприятие')
    vid = models.CharField(max_length=50, blank=False, default='Проект', verbose_name='Вид деятельности',
                          choices=VID
                          )

    dejat= models.CharField(max_length=200, null=False, verbose_name='Наименование деятельности/Причина переоформления')
    fact_adr = models.CharField(max_length=200, null=False,
                                 verbose_name='Фактический адрес осуществления деятельности')
    adres_Applicant = models.CharField(max_length=200, null=False,
                                       verbose_name='Юридический адрес заявителя, представителя заявителя')
    Otd = models.CharField(max_length=120, null=False, verbose_name='Отдел исполнитель', default= 'Гигиена детей и подростков',
                           choices=[
                                ('Гигиена детей и подростков', 'Гигиена детей и подростков'),
                                ('Гигиена труда', 'Гигиена труда'),
                                ('Эпид. отдел', 'Эпид. отдел'),
                                 ('Отдел санитарно-эпидемиологических заключений', 'Отдел санитарно-эпидемиологических заключений'),

                            ]
                            )
    sp = models.CharField(max_length=200, null=False, verbose_name='Способ направления документов', default="ПГУ",
                          choices=SPOSOB_NAPR)

    Vip = models.BooleanField(null=True, verbose_name='Выполнено', default=False)
    Prim = models.CharField(max_length=200, blank=True, verbose_name='Примечание')

    def __str__(self):
        return self.namber

    class Meta:  # Класс для названий нашей модели в админке
        verbose_name = 'Заявление на получение санитарно-эпидемиологического заключения, лицензии, свидетельства о государственной регистрации продукции'  # Надпись в единственном числе
        verbose_name_plural = 'заявления на получение санитарно-эпидемиологического заключения, лицензии, свидетельства о государственной регистрации продукции'  # Надпись во множественном числе
        ordering = ['namber']  # Сортировка полей (по возрастанию)


# Модель для хранения Решений
class Reestr_2(models.Model):
    TYP = [
                                  ('Установление санитарно-защитной зоны', 'Установление санитарно-защитной зоны'),
                                  ('Изменение санитарно-защитной зоны', 'Изменение санитарно-защитной зоны'),
                                  ('Сокращение санитарно-защитной зоны', 'Сокращение санитарно-защитной зоны'),
                              ]
    KL = [
                                  ('1', '1'),
                                  ('2', '2'),
                                  ('3', '3'),
                                  ('4', '4'),
                                  ('5', '5'),
                              ]
    namber = models.CharField(max_length=15, null=False, default=func2, verbose_name='Номер заявления')
    date_creation = models.DateTimeField(null=False, verbose_name='Дата регистрации заявления')
    date_rendering = models.DateTimeField(null=False, verbose_name='Дата оказания государственной услуги')
    fact_adr = models.CharField(max_length=200, blank=False, verbose_name='Фактический адрес объекта')
    cl = models.CharField(null=False,max_length=2,verbose_name='Класс опасности', default='5',
                              choices=KL
                              )
    Type_application = models.CharField(max_length=100, null=False, verbose_name='Тип заявления', default='Установление санитарно-защитной зоны',
                              choices=TYP
                              )
    Object = models.CharField(max_length=50, null=False, verbose_name='Тип объекта', default='Действующий',
                              choices=[
                                  ('Действующий', 'Действующий'),
                                  ('Проектируемый', 'Проектируемый'),
                                  ('Реконструированный', 'Реконструированный'),
                              ]
                              )
    Applicant = models.CharField(max_length=200, null=False, verbose_name='Наименование заявителя, представителя заявителя')
    adres_Applicant = models.CharField(max_length=200, null=False, verbose_name='Юридический адрес заявителя, представителя заявителя')
    Accredited_organization = models.CharField(max_length=200, blank=True, verbose_name='Аккредитованная организация, проводившая исследования')
    Accreditation_number = models.CharField (max_length=50, blank=True, verbose_name='Номер аттестата аккредитации')
    Name_obj = models.CharField(max_length=200, null=False, verbose_name='Наименование проекта')
    designer = models.CharField(max_length=200, null=False, verbose_name='Наименование проектировщика')
    adr = models.CharField(max_length=200, null=False, verbose_name='Юридический адрес проектировщика')
    conclusion_number = models.CharField(max_length=150, null=False, verbose_name='Номер экспертного заключения')
    accreditation = models.CharField(max_length=200, null=False, verbose_name='Номер аттестата аккредитации экспертной организации')
    name_acr = models.CharField(max_length=200, null=False, verbose_name='Кем выдано экспертное заключение')
    adr1 = models.CharField(max_length=200, null=False, verbose_name='Юридический адрес экспертной организации')
    SEZ1 = models.CharField(max_length=27, blank=True, verbose_name='Номер санитарно-эпидемиологического заключения')
    SEZ2 = models.CharField(null=False,max_length=40, verbose_name='Кем выдано', default='Роспотребнадзор',
                              choices=[
                                  ('Роспотребнадзор', 'Роспотребнадзор'),
                                  ('Иная организация', 'Иная организация'),
                              ]
                              )
    Vip = models.BooleanField(null=True, blank=True, verbose_name='Выполнено', default=False)
    def get_absolute_url(self):  # тэг url для объекта (Данный метод для вывода странички одной записи)
        return reverse('PR_SEZ', kwargs={'SEZ2': self.pk, 'namber': self.namber})
    def __str__(self):
        return self.namber

    class Meta:  # Класс для названий нашей модели в админке
        verbose_name = 'заявление на выдачу решения об установлении санитарно-защитной зоны'  # Надпись в единственном числе
        verbose_name_plural = 'заявления на выдачу решения об установлении санитарно-защитной зоны'  # Надпись во множественном числе
        ordering = ['namber']  # Сортировка полей (по возрастанию)

class Reestr1Summary(Reestr_1):
    class Meta:
        proxy = True
        verbose_name = 'Количество заявлений на получение санитарно-эпидемиологического заключения, лицензии, свидетельства о государственной регистрации продукции'
        verbose_name_plural = 'Количество заявлений на получение санитарно-эпидемиологического заключения, лицензии, свидетельства о государственной регистрации продукции'



class Reestr2Summary(Reestr_2):
    class Meta:
        proxy = True
        verbose_name = 'Количество заявлений на выдачу решений об установлении санитарно-защитной зоны'
        verbose_name_plural = 'Количество заявлений на выдачу решений об установлении санитарно-защитной зоны'


# Create your models here.

