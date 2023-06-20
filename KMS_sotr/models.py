from django.db import models
from django.urls import reverse, reverse_lazy

"""Модели приложения"""
class OPT_STAND(models.Model):
    title = models.CharField(max_length=200, blank=False, verbose_name='Название документа')
    date_creation = models.DateTimeField(blank=True, verbose_name='Дата документа')
    kr_op = models.TextField(max_length=200, blank=False, verbose_name='Краткое описание')
    silk = models.FileField(upload_to='KMS_OPT/%Y/%m/%d', blank=True, verbose_name='Ссылка для скачивания документа')

    class Meta:
        verbose_name = 'Оптимизированные стандарты'
        verbose_name_plural = 'Оптимизированные стандарты'

class ADM_REG(models.Model):
    title = models.CharField(max_length=200, blank=False, verbose_name='Название административного регламента')
    date_creation = models.DateTimeField(blank=True, verbose_name='Дата документа')
    kr_op = models.TextField(max_length=200, blank=False, verbose_name='Краткое описание')
    silk = models.FileField(upload_to='KMS_ADM/%Y/%m/%d', blank=True, verbose_name='Ссылка для скачивания документа')

    class Meta:
        verbose_name = 'Административный регламент'
        verbose_name_plural = 'Административные регламенты'

class NPA_SEZ(models.Model):
    title = models.CharField(max_length=200, blank=False, verbose_name='Название документа')
    date_creation = models.DateTimeField(blank=True, verbose_name='Дата документа')
    kr_op = models.TextField(max_length=200, blank=False, verbose_name='Краткое описание')
    silk = models.FileField(upload_to='KMS_SEZ/%Y/%m/%d', blank=True, verbose_name='Ссылка для скачивания документа')

    class Meta:
        verbose_name = 'НПА по СЭЗ'
        verbose_name_plural = 'НПА по СЭЗ'

class NPA_GOSREG(models.Model):
    title = models.CharField(max_length=200, blank=False, verbose_name='Название документа')
    date_creation = models.DateTimeField(blank=True, verbose_name='Дата документа')
    kr_op = models.TextField(max_length=200, blank=False, verbose_name='Краткое описание')
    silk = models.FileField(upload_to='KMS_GOSREG/%Y/%m/%d', blank=True, verbose_name='Ссылка для скачивания документа')

    class Meta:
        verbose_name = 'НПА по государственной регистрации продукции'
        verbose_name_plural = 'НПА по государственной регистрации продукции'


class NPA_LICENZ(models.Model):
    title = models.CharField(max_length=200, blank=False, verbose_name='Название документа')
    date_creation = models.DateTimeField(blank=True, verbose_name='Дата документа')
    kr_op = models.TextField(max_length=200, blank=False, verbose_name='Краткое описание')
    silk = models.FileField(upload_to='KMS_LICENZ/%Y/%m/%d', blank=True, verbose_name='Ссылка для скачивания документа')

    class Meta:
        verbose_name = 'НПА по лицензированию'
        verbose_name_plural = 'НПА по лицензированию'

class NPA_UVED(models.Model):
    title = models.CharField(max_length=200, blank=False, verbose_name='Название документа')
    date_creation = models.DateTimeField(blank=True, verbose_name='Дата документа')
    kr_op = models.TextField(max_length=200, blank=False, verbose_name='Краткое описание')
    silk = models.FileField(upload_to='KMS_UVED/%Y/%m/%d', blank=True, verbose_name='Ссылка для скачивания документа')

    class Meta:
        verbose_name = 'НПА по уведомлениям о начале осуществления предпринимательской деятельности'
        verbose_name_plural = 'НПА по уведомлениям о начале осуществления предпринимательской деятельности'

class NPA_SZZ(models.Model):
    title = models.CharField(max_length=200, blank=False, verbose_name='Название документа')
    date_creation = models.DateTimeField(blank=True, verbose_name='Дата документа')
    kr_op = models.TextField(max_length=200, blank=False, verbose_name='Краткое описание')
    silk = models.FileField(upload_to='KMS_SZZ/%Y/%m/%d', blank=True, verbose_name='Ссылка для скачивания документа')

    class Meta:
        verbose_name = 'НПА по санитарно-защитным зонам'
        verbose_name_plural = 'НПА по санитарно-защитным зонам'



