from django.db import models
from django.db import models
from core.models import Reestr_1, Reestr_2

class OTK(models.Model):
    Nomer1 = models.CharField(max_length=60, blank=True,
                             verbose_name='Номер письма', unique=True)
    date_creation = models.DateTimeField(null=True, verbose_name='Дата документа')
    prich = models.CharField(max_length=50, blank=False,verbose_name='Причина отказа')
    vidano = models.CharField(max_length=150, blank=True, verbose_name='Кем выдано',
                              )

    class Meta:
        verbose_name = 'Отказы'
        verbose_name_plural = 'Отказы'


    def __str__(self):
        return 'Письмо № {}'.format(self.Nomer1)


class OTKItem(models.Model):
    otk = models.ForeignKey(OTK, verbose_name='Номер письма', related_name='items', null=True, on_delete=models.SET_NULL)
    product1 = models.ForeignKey(Reestr_1, verbose_name='Заявление', related_name='order_items1', null=True, on_delete=models.SET_NULL)
    product2 = models.ForeignKey(Reestr_2,  verbose_name='Заявление2', related_name='order_items2', null=True, on_delete=models.SET_NULL)
    status1 = models.CharField(max_length=150, null=True, verbose_name='Статус', default='Создан',
                              choices=[
                                  ('Отказ в оказании государственной услуги', 'Отказ в оказании государственной услуги'),
                              ]
                              )
    class Meta:
        verbose_name = 'Отказы в выдаче документов'
        verbose_name_plural = 'Отказы в выдаче документов'


    def __str__(self):
        return '{}'.format(self.otk)


class OTKAZSummary(OTK):
    class Meta:
        proxy = True
        verbose_name = 'Количество отказов в выдаче документов'
        verbose_name_plural = 'Количество отказов в выдаче документов'


# Create your models here.
