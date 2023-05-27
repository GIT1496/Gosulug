from django.db import models
from django.db import models
from core.models import Reestr_1, Reestr_2
from multiselectfield import MultiSelectField

class SEZ1(models.Model):
    Nomer = models.CharField(max_length=60, blank=True,
                             verbose_name='Номер санитарно-эпидемиологического заключения, лицензии, свидетельства о государственной регистрации продукции', unique=True)
    date_creation = models.DateTimeField(null=True, verbose_name='Дата документа')
    tipogr = models.CharField(max_length=50, blank=False,verbose_name='Типографский номер бланка')
    g = (
                                 ('СанПиН 1.2.3685-21 "Гигиенические нормативы и требования к обеспечению безопасности и (или) безвредности для человека факторов среды обитания"', 'СанПиН 1.2.3685-21 "Гигиенические нормативы и требования к обеспечению безопасности и (или) безвредности для человека факторов среды обитания"'),
                                 ('СанПиН 2.3/2.4.3590-20 "Санитарно-эпидемиологические требования к организации общественного питания населения"', 'СанПиН 2.3/2.4.3590-20 "Санитарно-эпидемиологические требования к организации общественного питания населения"'),
                                 ('Переоформление','Переоформление'),
    )
    sootv = MultiSelectField(max_length=500, choices=g, verbose_name='Соответствует: ', null=True, blank=False)
    Pereof = models.CharField(max_length=30, blank=True, verbose_name='Номер переоформляемого СЭЗ')
    vidano = models.CharField(max_length=150, blank=True, verbose_name='Кем выдано')
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
    licenz = models.CharField(max_length=300, blank=False,verbose_name='Лицензиат')
    INN = models.IntegerField(blank=True)
    OGRN = models.IntegerField(blank=True)

    UR = models.CharField(max_length=300, blank=False,verbose_name='Юридический адрес лицензиата')
    g = (
        ('Деятельность в области использования возбудителей инфекционных заболеваний человека и животных (за исключением случая, если указанная деятельность осуществляется в медицинских целях) и генно-инженерно-модифицированных организмов III и IV степеней потенциальной опасности, осуществляемой в замкнутых системах.',
         'Деятельность в области использования возбудителей инфекционных заболеваний человека и животных (за исключением случая, если указанная деятельность осуществляется в медицинских целях) и генно-инженерно-модифицированных организмов III и IV степеней потенциальной опасности, осуществляемой в замкнутых системах'),
        ('Деятельность в области использования источников ионизирующего излучения (генерирующих) (за исключением случая, если эти источники используются в медицинской деятельности).','Деятельность в области использования источников ионизирующего излучения (генерирующих) (за исключением случая, если эти источники используются в медицинской деятельности).'))
    vid = models.CharField (max_length=500, blank=False, choices=g, default='Деятельность в области использования возбудителей инфекционных заболеваний человека и животных (за исключением случая, если указанная деятельность осуществляется в медицинских целях) и генно-инженерно-модифицированных организмов III и IV степеней потенциальной опасности, осуществляемой в замкнутых системах.',  verbose_name='Вид деятельности')
    mesto = models.CharField (max_length=500, blank=False,  verbose_name='Место осуществления деятельности')

    class Meta:
        verbose_name = 'Лицензии'
        verbose_name_plural = 'Лицензии'

    def __str__(self):
        return 'SEZ {}'.format(self.Nomer)

class RESH1(models.Model):
    namber = models.CharField(max_length=60, blank=False,
                             verbose_name='Номер Решения', unique=True)
    date_creation = models.DateTimeField(blank=False, verbose_name='Дата документа')
    applic = models.CharField(max_length=300, blank=False, verbose_name='Заявитель (представитель заявителя)')
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

# Create your models here.
