from decimal import Decimal
from django.conf import settings
from core.models import Reestr_1, Reestr_2

"""Классы для работы с ID сессии и добавления выбранных элементов в сессию"""

class Basket_resh(object):
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)

        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def save(self):
        # Обновление ключа "basket" в сессии
        self.session[settings.BASKET_SESSION_ID] = self.basket
        # Отметка сессии в опции "измененный", для обновления и сохранения данных
        self.session.modified = True

    def add(self, product, count_product=1, update_count=False):
        prod_pk = str(product.pk)

        # Проверка наличия в корзине (если нет в корзине, то добавляем)
        if prod_pk not in self.basket:
            self.basket[prod_pk] = {
                'count_prod': 0,
                'namber_prod': str(product.namber)
            }

        # Обновление количества в корзине
        if update_count:
            self.basket[prod_pk]['count_prod'] = count_product
        else:
            self.basket[prod_pk]['count_prod'] = count_product

        # Сохранение корзины в сессию
        self.save()

    def remove(self, product):
        prod_pk = str(product.pk)

        # Если удаляемое заявление лежит в корзине, то очищаем его ключ (и данные о нём)
        if prod_pk in self.basket:
            del self.basket[prod_pk]
            self.save()

    def clear(self):

        del self.session[settings.BASKET_SESSION_ID]

        self.session.modified = True

    def __len__(self):
        return sum(int(item['count_prod']) for item in self.basket.values())

    def __iter__(self):
        # Получение первичных ключей
        list_prod_pk = self.basket.keys()
        print(list_prod_pk)

        # Загрузка данных из БД
        list_prod_obj = Reestr_2.objects.filter(pk__in=list_prod_pk)
        print(list_prod_obj)

        # Копирование корзины для дальнейшей работы
        basket = self.basket.copy()
        # Перебор и добавление объектов(записей) из БД

        for prod_obj in list_prod_obj:
            basket[str(prod_obj.pk)]['RES1'] = prod_obj
            print(prod_obj)

        for item in basket.values():
            item['total_price'] = item['namber_prod']
            yield item


class Basket(object):
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)

        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def save(self):
        # Обновление ключа "basket" в сессии
        self.session[settings.BASKET_SESSION_ID] = self.basket
        # Отметка сессии в опции "измененный", для обновления и сохранения данных
        self.session.modified = True

    def add(self, product, count_product=1, update_count=False):
        prod_pk = str(product.pk)

        # Проверка наличия в корзине (если нет в корзине, то добавляем)
        if prod_pk not in self.basket:
            self.basket[prod_pk] = {
                'count_prod': 0,
                'namber_prod': str(product.namber)
            }

        # Обновление количества в корзине
        if update_count:
            self.basket[prod_pk]['count_prod'] = count_product
        else:
            self.basket[prod_pk]['count_prod'] = count_product

        # Сохранение корзины в сессию
        self.save()

    def remove(self, product):
        prod_pk = str(product.pk)

        # Если удаляемое заявление лежит в корзине, то очищаем его ключ (и данные о нём)
        if prod_pk in self.basket:
            del self.basket[prod_pk]
            self.save()


    def clear(self):

        del self.session[settings.BASKET_SESSION_ID]

        self.session.modified = True

    def __len__(self):
        return sum(int(item['count_prod']) for item in self.basket.values())

    def __iter__(self):
        # Получение первичных ключей
        list_prod_pk = self.basket.keys()
        print(list_prod_pk)

        # Загрузка данных из БД
        list_prod_obj = Reestr_1.objects.filter(pk__in=list_prod_pk)
        print(list_prod_obj)

        # Копирование корзины для дальнейшей работы
        basket = self.basket.copy()
        # Перебор и добавление объектов(записей) из БД

        for prod_obj in list_prod_obj:
            basket[str(prod_obj.pk)]['SEZ'] = prod_obj
            print(prod_obj)

        for item in basket.values():
            item['total_price'] = item['namber_prod']
            yield item


