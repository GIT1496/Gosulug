from django.core import serializers
from django.shortcuts import render
from django.db.models import Count,F,Sum,Avg
from django.db.models.functions import ExtractYear,ExtractMonth
from django.http import JsonResponse
from SANZ_1.models import SEZ1, LIC1, SVID, Pereoformlen
from .utils import (
    months,colorDanger,
    colorPrimary,colorSuccess,
    generate_color_palette,get_year_dict)


"""Модуль для дашбордов по СЭЗ"""
def display_charts3(request):
    return render(request, 'analys/charts3.html', {})

def filter_options_sez(request):
    merged_purchases=SEZ1.objects.annotate(
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




def get_SEZ(request, year):
    sez=SEZ1.objects.filter(date_creation__year=year)
    merged_purchases=sez.annotate(month=ExtractMonth('date_creation')).values(
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
        'title':f'Количество выданных СЭЗ в {year}',
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

def get_LIC(request, year):
    lic=LIC1.objects.filter(date_creation__year=year)
    merged_purchases=lic.annotate(month=ExtractMonth('date_creation')).values(
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
        'title':f'Количество выданных лицензий в {year}',
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
def get_SVID(request, year):
    sv=SVID.objects.filter(date_creation__year=year)
    merged_purchases=sv.annotate(month=ExtractMonth('date_creation')).values(
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
        'title':f'Количество выданных свидетельств о государственной регистрации продукции в {year}',
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

def get_PERE(request, year):
    PER=Pereoformlen.objects.filter(date__year=year)
    merged_purchases=PER.annotate(month=ExtractMonth('date')).values(
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
        'title':f'Количество переоформленных документов в {year}',
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
# def SEZ_date_vix(request, year):
#     resh = SEZ1.objects.filter(date_creation__year=year)
#
#     return JsonResponse({
#         'title': f'Статистика выполненных заявлений в {year}',
#         'data': {
#             'labels': ['Выполнено', 'Невыполнено'],
#             'datasets': [{
#                 'label': 'Месяц',
#                 'backgroundColor': generate_color_palette(12),
#                 'borderColor': generate_color_palette(9),
#                 'data': [
#                     resh.filter(deistv=).count(),
#                     resh.filter(Vip=False).count(),
#                 ],
#             }]
#         },
#     })

