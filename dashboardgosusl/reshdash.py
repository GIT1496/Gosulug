from django.core import serializers
from django.shortcuts import render
from django.db.models import Count,F,Sum,Avg
from django.db.models.functions import ExtractYear,ExtractMonth
from django.http import JsonResponse
from core.models import Reestr_2
from .utils import (
    months,colorDanger,
    colorPrimary,colorSuccess,
    generate_color_palette,get_year_dict)



def display_charts2(request):
    return render(request, 'analys/charts2.html', {})

def filter_options_resh(request):
    merged_purchases=Reestr_2.objects.annotate(
        year=ExtractYear(
            'date_creation'
        )).values(
            'year'
            ).order_by(
                '-year'
                ).distinct()
    options= [purchase['year'] for purchase in merged_purchases]

    return JsonResponse(data={
        'options':options
    })




def get_annual_sajav2(request, year):
    resh=Reestr_2.objects.filter(date_creation__year=year)
    merged_purchases=resh.annotate(month=ExtractMonth('date_creation')).values(
        'month'
    ).annotate(
        average=Count(
            'id'
        )
    ).values(
        'month',
        'average'
    ).order_by('month')
    sales_dict=get_year_dict()
    for merge in merged_purchases:
        sales_dict[months[merge['month']-1]]=round(merge['average'], 2)

    return JsonResponse({
        'title':f'Количество заявлений в {year}',
        'data':{
            'labels':list(sales_dict.keys()),
            'datasets':[{
                'label':'Количество',
                'backgroundColor':generate_color_palette(7),
                'borderColor':generate_color_palette(5),
                'data':list(sales_dict.values())
            }]
        }
    })



def sajav_vip_chart_resh(request, year):
    resh = Reestr_2.objects.filter(date_creation__year=year)

    return JsonResponse({
        'title': f'Статистика выполненных заявлений в {year}',
        'data': {
            'labels': ['Выполнено', 'Невыполнено'],
            'datasets': [{
                'label': 'Месяц',
                'backgroundColor': generate_color_palette(12),
                'borderColor': generate_color_palette(9),
                'data': [
                    resh.filter(Vip=True).count(),
                    resh.filter(Vip=False).count(),
                ],
            }]
        },
    })

def RESH(request, year):
    resh = Reestr_2.objects.filter(date_creation__year=year)
    merged_purchases = resh.values('Type_application').annotate(count=Count('id'))\
        .values('Type_application', 'count').order_by('Type_application')

    tp_dict = dict()

    for sp in Reestr_2.TYP:
        tp_dict[sp[1]] = 0

    for group in merged_purchases:
        tp_dict[dict(Reestr_2.TYP)[group['Type_application']]] = group['count']

    return JsonResponse({
        'title': f'Заявления на СЗЗ по типу в {year}',
        'data': {
            'labels': list(tp_dict.keys()),
            'datasets': [{
                'label': 'Месяц',
                'backgroundColor': generate_color_palette(len(tp_dict)),
                'borderColor': generate_color_palette(len(tp_dict)),
                'data': list(tp_dict.values()),
            }]
        },
    })

def kl(request, year):
    resh = Reestr_2.objects.filter(date_creation__year=year)
    merged_purchases = resh.values('cl').annotate(count=Count('id'))\
        .values('cl', 'count').order_by('cl')

    kl_dict = dict()

    for sp in Reestr_2.KL:
        kl_dict[sp[1]] = 0

    for group in merged_purchases:
        kl_dict[dict(Reestr_2.KL)[group['cl']]] = group['count']

    return JsonResponse({
        'title': f'Заявления на СЗЗ по классу опасности {year}',
        'data': {
            'labels': list(kl_dict.keys()),
            'datasets': [{
                'label': 'Месяц',
                'backgroundColor': generate_color_palette(len(kl_dict)),
                'borderColor': generate_color_palette(len(kl_dict)),
                'data': list(kl_dict.values()),
            }]
        },
    })
