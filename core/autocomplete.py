from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from core.models import Reestr_1
from  core.forms import SEZform
from django.http import HttpResponse

from django.views.generic import View
from django.http import JsonResponse
from django.core import serializers
from core.models import Reestr_1, Reestr_2
from OTKAZ.models import OTK

class MyModelAutocompleteView(View):
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term')
        p = Reestr_1.objects.filter(predpr__icontains=term)
        results = []
        for predpr in p:
            predpr_json = {}
            predpr_json['id'] = predpr.id
            predpr_json['label'] = predpr.predpr
            predpr_json['value'] = predpr.predpr
            results.append(predpr_json)
            print(predpr_json)
        return JsonResponse(results, safe=False)

class ADRRES1AutocompleteView(View):
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term')
        ad = Reestr_1.objects.filter(fact_adr__icontains=term)
        results = []
        for adr in ad:
            adr_json = {}
            adr_json['id'] = adr.id
            adr_json['label'] = adr.fact_adr
            adr_json['value'] = adr.fact_adr
            results.append(adr_json)
            print(adr_json)
        return JsonResponse(results, safe=False)

class VIDAutocompleteView(View):
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term')
        dej = Reestr_1.objects.filter(dejat__icontains=term)
        results = []
        for dj in dej:
            dj_json = {}
            dj_json['id'] = dj.id
            dj_json['label'] = dj.dejat
            dj_json['value'] = dj.dejat
            results.append(dj_json)
            print(dj_json)
        return JsonResponse(results, safe=False)

class APAutocompleteView(View):
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term')
        ad = Reestr_1.objects.filter(adres_Applicant__icontains=term)
        results = []
        for apl in ad:
            apl_json = {}
            apl_json['id'] = apl.id
            apl_json['label'] = apl.adres_Applicant
            apl_json['value'] = apl.adres_Applicant
            results.append(apl_json)
            print(apl_json)
        return JsonResponse(results, safe=False)

class FCADRautocompView(View):
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term')
        au = Reestr_2.objects.filter(fact_adr__icontains=term)
        results = []
        for adr in au:
            apl_json = {}
            apl_json['id'] = adr.id
            apl_json['label'] = adr.fact_adr
            apl_json['value'] = adr.fact_adr
            results.append(apl_json)
            print(apl_json)
        return JsonResponse(results, safe=False)

class APautocompView(View):
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term')
        apl = Reestr_2.objects.filter(Applicant__icontains=term)
        results = []
        for ap in apl:
            apl_json = {}
            apl_json['id'] = ap.id
            apl_json['label'] = ap.Applicant
            apl_json['value'] = ap.Applicant
            results.append(apl_json)
            print(apl_json)
        return JsonResponse(results, safe=False)

class ADRAPautocompView(View):
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term')
        apl = Reestr_2.objects.filter(adres_Applicant__icontains=term)
        results = []
        for adrap in apl:
            apl_json = {}
            apl_json['id'] = adrap.id
            apl_json['label'] = adrap.adres_Applicant
            apl_json['value'] = adrap.adres_Applicant
            results.append(apl_json)
            print(apl_json)
        return JsonResponse(results, safe=False)

class ACRautocompView(View):
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term')
        acc = Reestr_2.objects.filter(Accredited_organization__icontains=term)
        results = []
        for acred in acc:
            apl_json = {}
            apl_json['id'] = acred.id
            apl_json['label'] = acred.Accredited_organization
            apl_json['value'] = acred.adres_Applicant
            results.append(apl_json)
            print(apl_json)
        return JsonResponse(results, safe=False)
class NACRautocompView(View):
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term')
        acc = Reestr_2.objects.filter(Accreditation_number__icontains=term)
        results = []
        for n in acc:
            apl_json = {}
            apl_json['id'] = n.id
            apl_json['label'] = n.Accreditation_number
            apl_json['value'] = n.Accreditation_number
            results.append(apl_json)
            print(apl_json)
        return JsonResponse(results, safe=False)

class DEJautocompView(View):
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term')
        des = Reestr_2.objects.filter(designer__icontains=term)
        results = []
        for d in des:
            apl_json = {}
            apl_json['id'] = d.id
            apl_json['label'] = d.designer
            apl_json['value'] = d.designer
            results.append(apl_json)
            print(apl_json)
        return JsonResponse(results, safe=False)

class ADRDESautocompView(View):
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term')
        adrdes = Reestr_2.objects.filter(adr__icontains=term)
        results = []
        for adr in adrdes:
            apl_json = {}
            apl_json['id'] = adr.id
            apl_json['label'] = adr.adr
            apl_json['value'] = adr.adr
            results.append(apl_json)
            print(apl_json)
        return JsonResponse(results, safe=False)

class ACCRESDautocompView(View):
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term')
        accred = Reestr_2.objects.filter(accreditation__icontains=term)
        results = []
        for ac in accred:
            apl_json = {}
            apl_json['id'] = ac.id
            apl_json['label'] = ac.accreditation
            apl_json['value'] = ac.accreditation
            results.append(apl_json)
            print(apl_json)
        return JsonResponse(results, safe=False)

class NAMEautocompView(View):
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term')
        naccred = Reestr_2.objects.filter(name_acr__icontains=term)
        results = []
        for nam in naccred:
            apl_json = {}
            apl_json['id'] = nam.id
            apl_json['label'] = nam.name_acr
            apl_json['value'] = nam.name_acr
            results.append(apl_json)
            print(apl_json)
        return JsonResponse(results, safe=False)

class ADR1autocompView(View):
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term')
        adr1 = Reestr_2.objects.filter(adr1__icontains=term)
        results = []
        for adr in adr1:
            apl_json = {}
            apl_json['id'] = adr.id
            apl_json['label'] = adr.adr1
            apl_json['value'] = adr.adr1
            results.append(apl_json)
            print(apl_json)
        return JsonResponse(results, safe=False)

class OTKautocompView(View):
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term')
        otk = OTK.objects.filter(prich__icontains=term)
        results = []
        for o in otk:
            apl_json = {}
            apl_json['id'] = o.id
            apl_json['label'] = o.prich
            apl_json['value'] = o.prich
            results.append(apl_json)
            print(apl_json)
        return JsonResponse(results, safe=False)


# import json
#
# def get_places(request):
#   if request.is_ajax():
#     q = request.GET.get('term', '')
#     places = Reestr_1.objects.filter(predpr__icontains=q)
#     results = []
#     for pl in places:
#       place_json = {}
#       place_json = pl.predpr
#       results.append(place_json)
#     data = json.dumps(results)
#   else:
#     data = 'fail'
#   mimetype = 'application/json'
#   return HttpResponse(data, mimetype)













# @csrf_exempt
# @require_POST
# def search(request):
#     query = request.POST.get('query', '')
#     results = Reestr_1.objects.filter(name__icontains=query)
#     data = [{'id': r.id, 'predpr': r.predpr} for r in results]
#     return JsonResponse({'data': data})