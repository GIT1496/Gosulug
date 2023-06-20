from django.db import models
from django.db import models
from core.models import Reestr_1, Reestr_2
from multiselectfield import MultiSelectField

"""Модели приложения"""
class SEZ1(models.Model):
    Nomer = models.CharField(max_length=60, blank=True,
                             verbose_name='Номер санитарно-эпидемиологического заключения, лицензии, свидетельства о государственной регистрации продукции', unique=True)
    date_creation = models.DateTimeField(null=True, verbose_name='Дата документа')
    tipogr = models.CharField(max_length=50, blank=False,verbose_name='Типографский номер бланка')
    g = (
                                 ('СанПиН 1.2.3685-21 "Гигиенические нормативы и требования к обеспечению безопасности и (или) безвредности для человека факторов среды обитания"', 'СанПиН 1.2.3685-21 "Гигиенические нормативы и требования к обеспечению безопасности и (или) безвредности для человека факторов среды обитания"'),
                                 ('СанПиН 2.3/2.4.3590-20 "Санитарно-эпидемиологические требования к организации общественного питания населения"', 'СанПиН 2.3/2.4.3590-20 "Санитарно-эпидемиологические требования к организации общественного питания населения"'),

    )
    sootv = MultiSelectField(max_length=500, choices=g, verbose_name='Соответствует: ', null=True, blank=False)
    vidano = models.CharField(max_length=150, blank=True, verbose_name='Кем выдано', default='Управление Роспотребнадзора по Архангельской области')
    deistv = models.DateTimeField(null=True, blank=True, verbose_name='Действует до')

    class Meta:
        verbose_name = 'СЭЗ'
        verbose_name_plural = 'СЭЗ'



    def __str__(self):
        return 'SEZ {}'.format(self.Nomer)

class LIC1(models.Model):
    Nomer = models.CharField(max_length=60, blank=True,
                             verbose_name='Номер лицензии', unique=True)
    date_creation = models.DateTimeField(blank=False, verbose_name='Дата документа')

    g = (
        ('Деятельность в области использования возбудителей инфекционных заболеваний человека и животных ', 'Деятельность в области использования возбудителей инфекционных заболеваний человека и животных'),
        ('Деятельность в области использования источников ионизирующего излучения (генерирующих)','Деятельность в области использования источников ионизирующего излучения (генерирующих)'))
    vid = models.CharField (max_length=500, blank=False, choices=g, default='Деятельность в области использования возбудителей инфекционных заболеваний человека и животных',  verbose_name='Вид деятельности')

    class Meta:
        verbose_name = 'Лицензии'
        verbose_name_plural = 'Лицензии'

    def __str__(self):
        return 'SEZ {}'.format(self.Nomer)

class SVID(models.Model):
    Nomer = models.CharField(max_length=30, verbose_name='Номер Свидетельства о государственной регистрации', unique=True, blank=False)
    date_creation = models.DateTimeField(blank=False, verbose_name='Дата документа')
    tipogr = models.CharField(max_length=30, verbose_name='Типографский номер бланка', blank=True)
    obl = models.CharField(max_length=300, verbose_name='Область применения', blank=False)
    Svid_vid = models.CharField(max_length=500, verbose_name='Сведетельство выдано', blank=False)
    firm = models.CharField(max_length=200, verbose_name='Фирма получатель', blank=False)
    Norm = models.CharField(max_length=200, verbose_name='Нормативная документация', blank=False)

    class Meta:
        verbose_name = 'Свидетельства о государственной регистрации продукции'
        verbose_name_plural = 'Свидетельства о государственной регистрации продукции'

class Pereoformlen(models.Model):
    nomer = models.CharField(max_length=200, verbose_name='Номер переоформляемого документа и дата', blank=False)
    nomer2 = models.CharField(max_length=200, verbose_name='Номер нового документа', blank=False)
    date = models.DateTimeField(blank=False, verbose_name='Дата новго документа')
    prich = models.CharField(max_length=200, verbose_name='Причина переоформления документа', blank=False)

    class Meta:
        verbose_name = 'Переоформленные документы'
        verbose_name_plural = 'Переоформленные документы'

class RESH1(models.Model):
    namber = models.CharField(max_length=60, blank=False,
                             verbose_name='Номер Решения', unique=True)
    date_creation = models.DateTimeField(blank=False, verbose_name='Дата документа')
    applic = models.CharField(max_length=300, blank=False, verbose_name='Заявитель (представитель заявителя)')
    kl = models.CharField(max_length=2, blank=True,  verbose_name='Класс опасности объекта')
    photo = models.FileField(upload_to='pdf/%Y/%m/%d', null=True, verbose_name='Скан решения')

    class Meta:
        verbose_name = 'Решения'
        verbose_name_plural = 'Решения'

    def __str__(self):
        return 'SEZ {}'.format(self.namber)


class RESHItem(models.Model):
    resh = models.ForeignKey(RESH1, verbose_name='Номер решения', related_name='items3', null=True, on_delete=models.SET_NULL)
    sajav = models.ForeignKey(Reestr_2, verbose_name='Номер заявления', related_name='items4', null=True, blank=True,
                            on_delete=models.SET_NULL)
    status = models.CharField(max_length=150, null=True, verbose_name='Статус', default='-',
                              choices=[
                                  ('-', '-'),
                                  ('Услуга оказана', 'Услуга оказана'),
                              ]
                              )



class SEZItem(models.Model):
    SEZ = models.ForeignKey(SEZ1, verbose_name='Номер СЭЗ', related_name='items_SEZ', null=True, on_delete=models.SET_NULL)
    LIC = models.ForeignKey(LIC1, verbose_name='Номер лицензии', related_name='items_SEZ_LIC', null=True, blank=True, on_delete=models.SET_NULL)
    SV = models.ForeignKey(SVID, verbose_name='Номер свидетельства о государственной регистрации', related_name='items_SEZ_SVID', null=True, blank=True, on_delete=models.SET_NULL)
    PER = models.ForeignKey(Pereoformlen, verbose_name='Номер переоформленного документа', related_name='items_SEZ_Pere', null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Reestr_1, verbose_name='Заявление', related_name='order_items', null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=150, null=True, verbose_name='Статус', default='-',
                              choices=[
                                  ('-', '-'),
                                  ('Услуга оказана', 'Услуга оказана'),
                              ]
                              )
    class Meta:
        verbose_name = 'Санитарно-эпидемиологические заключения'
        verbose_name_plural = 'Санитарно-эпидемиологические заключения'


    def __str__(self):
        return '{}'.format(self.SEZ)



class SEZSummary(SEZ1):
    class Meta:
        proxy = True
        verbose_name = 'Количество выданных СЭЗ'
        verbose_name_plural = 'Количество выданных СЭЗ'

class LICSummary(LIC1):
    class Meta:
        proxy = True
        verbose_name = 'Количество выданных Лицензий'
        verbose_name_plural = 'Количество выданных Лицензий'

class SVIDSummary(SVID):
    class Meta:
        proxy = True
        verbose_name = 'Количество выданных Свидетельств'
        verbose_name_plural = 'Количество выданных Свидетельств'

# class PereSummary(Pereoformlen):
#     proxy = True
#     verbose_name = 'Количество переоформленных документов'
#     verbose_name_plural = 'Количество переоформленных документов'

# Create your models here.
