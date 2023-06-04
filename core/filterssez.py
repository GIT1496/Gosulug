from django.shortcuts import render, get_object_or_404, redirect
from core.models import Reestr_1, Reestr_2
from datetime import datetime, timedelta
def Reestr1_list(request):
    """Вывод всех заявлений
    """
    news = Reestr_1.objects.filter(Vip=False)
    return render(request, "reestr/SEZ/SEZ_filter_list.html", {"news": news})
def Reestr2_list(request):
    """Вывод всех заявлений
    """
    list1 = Reestr_2.objects.filter(Vip=False)
    return render(request, "reestr/Reshen/RESH_filter_list.html", {"list1": list1})

def Reestr1_filter(request, pk):
    """ Фильтр заявлений по дате
    """
    news = Reestr_1.objects.all()
    if pk == 1:
        now = datetime.now() - timedelta(minutes=60*24*7)
        news = news.filter(date_creation__gte=now, Vip=False)
    elif pk == 2:
        now = datetime.now() - timedelta(minutes=60*24*30)
        news = news.filter(date_creation__gte=now, Vip=False)
    elif pk == 3:
        news = news.filter(Vip=False)

    return render(request, "reestr/SEZ/SEZ_filter_list.html", {"news": news})


def Reestr2_filter(request, pk):
    """ Фильтр заявлений по дате
    """
    list1 = Reestr_2.objects.all()
    if pk == 1:
        now = datetime.now() - timedelta(minutes=60*24*7)
        list1 = list1 .filter(date_creation__gte=now, Vip=False)
    elif pk == 2:
        now = datetime.now() - timedelta(minutes=60*24*30)
        list1 = list1 .filter(date_creation__gte=now, Vip=False)
    elif pk == 3:
        list1 = list1.filter(Vip=False)

    return render(request, "reestr/Reshen/RESH_filter_list.html", {"list1": list1})