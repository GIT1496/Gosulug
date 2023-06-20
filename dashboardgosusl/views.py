from django.http import JsonResponse
from django.shortcuts import render
from core.models import Reestr_1
from django.core import serializers
from django.shortcuts import render
from django.db.models import Count,F,Sum,Avg
from django.db.models.functions import ExtractYear,ExtractMonth
from django.http import JsonResponse
from core.models import Reestr_1, Reestr_2
from .utils import (
    months,colorDanger,
    colorPrimary,colorSuccess,
    generate_color_palette,get_year_dict)
# Create your views here.

"""Дашборд статистика по заявлениям на решения, деятельность и т.д."""
def display_charts(request):
    return render(request, 'analys/charts.html', {})

def filter_options(request):
    merged_purchases=Reestr_1.objects.annotate(
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




def get_annual_sajav(request, year):
    sajav=Reestr_1.objects.filter(date_creation__year=year)
    merged_purchases=sajav.annotate(month=ExtractMonth('date_creation')).values(
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



def sajav_vip_chart(request, year):
    sajav = Reestr_1.objects.filter(date_creation__year=year)

    return JsonResponse({
        'title': f'Статистика выполненных заявлений в {year}',
        'data': {
            'labels': ['Выполнено', 'Невыполнено'],
            'datasets': [{
                'label': 'Месяц',
                'backgroundColor': generate_color_palette(12),
                'borderColor': generate_color_palette(9),
                'data': [
                    sajav.filter(Vip=True).count(),
                    sajav.filter(Vip=False).count(),
                ],
            }]
        },
    })

def GMU_1(request, year):
    purchases = Reestr_1.objects.filter(date_creation__year=year)
    merged_purchases = purchases.values('sp').annotate(count=Count('id'))\
        .values('sp', 'count').order_by('sp')

    sp_dict = dict()

    for sp in Reestr_1.SPOSOB_NAPR:
        sp_dict[sp[1]] = 0

    for group in merged_purchases:
        sp_dict[dict(Reestr_1.SPOSOB_NAPR)[group['sp']]] = group['count']

    return JsonResponse({
        'title': f'Способ направления документов в {year}',
        'data': {
            'labels': list(sp_dict.keys()),
            'datasets': [{
                'label': 'Месяц',
                'backgroundColor': generate_color_palette(len(sp_dict)),
                'borderColor': generate_color_palette(len(sp_dict)),
                'data': list(sp_dict.values()),
            }]
        },
    })

def vid_chart(request, year):
    purchases = Reestr_1.objects.filter(date_creation__year=year)
    merged_purchases = purchases.values('vid').annotate(count=Count('id'))\
        .values('vid', 'count').order_by('vid')

    vid_dict = dict()

    for sp in Reestr_1.VID:
        vid_dict[sp[1]] = 0

    for group in merged_purchases:
        vid_dict[dict(Reestr_1.VID)[group['vid']]] = group['count']

    return JsonResponse({
        'title': f'Количество заявлений в {year}',
        'data': {
            'labels': list(vid_dict.keys()),
            'datasets': [{
                'label': 'Количество заявлений',
                'backgroundColor': generate_color_palette(len(vid_dict)),
                'borderColor': generate_color_palette(len(vid_dict)),
                'data': list(vid_dict.values()),
            }]
        },
    })




def dashboard_with_pivot(request):
    return render(request, 'analys/dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = Reestr_1.objects.all()
    data = serializers.serialize('json', dataset)
    print(data)
    return JsonResponse(data, safe=False)


