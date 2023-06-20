from SANZ_1.models import SEZItem, RESHItem, Reestr_2, Reestr_1
from OTKAZ.models import OTKItem
from KMS_sotr.models import NPA_SEZ, NPA_UVED, NPA_SZZ, NPA_GOSREG, NPA_LICENZ, OPT_STAND, ADM_REG
from django.db.models import Q
from django.views.generic import ListView

"""Модуль для поиска информации в информационной системе"""

# Классы для поиска информации
class SearchResultsView(ListView):
    model = SEZItem
    template_name = 'reestr/search/search_results.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = SEZItem.objects.filter(
             Q(SEZ__Nomer__icontains=query) | Q(LIC__Nomer__icontains=query) | Q(SV__Nomer__icontains=query)
             | Q(PER__nomer2__icontains=query) | Q(product__namber__icontains=query) | Q(product__predpr__icontains=query)| Q(product__fact_adr__icontains=query)
        )
        return object_list



class SearchResultsView1(ListView):
    model = OTKItem
    template_name = 'reestr/search/search_results1.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = OTKItem.objects.filter(
             Q(otk__Nomer1__icontains=query) | Q(product1__predpr__icontains=query) | Q(product1__fact_adr__icontains=query)
        )
        return object_list


class SearchResultsView2(ListView):
    model = RESHItem
    template_name = 'reestr/search/search_results2.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = RESHItem.objects.filter(
             Q(resh__namber__icontains=query) | Q(sajav__Applicant__icontains=query) | Q(sajav__fact_adr__icontains=query)
        )
        return object_list

class SearchResultsView3(ListView):
    model = Reestr_2
    template_name = 'reestr/search/search_results3.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = Reestr_2.objects.filter(
              Q(namber__icontains=query) | Q(fact_adr__icontains=query) | Q(Applicant__icontains=query), Vip=False
        )
        return object_list

class SearchResultsView4(ListView):
    model = Reestr_1
    template_name = 'reestr/search/search_results4.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = Reestr_1.objects.filter(
              Q(namber__icontains=query) | Q(predpr__icontains=query) | Q(fact_adr__icontains=query), Vip=False,
        )
        return object_list

class SearchResultsView5(ListView):
    model = OTKItem
    template_name = 'reestr/search/search_results5.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = OTKItem.objects.filter(
            Q(otk__Nomer1__icontains=query) | Q(product2__fact_adr__icontains=query) | Q(product2__Name_obj__icontains=query) | Q(product2__Applicant__icontains=query)
        )
        return object_list


class SearchResultsView6(ListView):
    model = NPA_SEZ
    template_name = 'reestr/search/search_results6.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = NPA_SEZ.objects.filter(
            Q(title__icontains=query) | Q(kr_op__icontains=query)
        )
        return object_list

class SearchResultsView7(ListView):
    model = NPA_UVED
    template_name = 'reestr/search/search_results7.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = NPA_UVED.objects.filter(
            Q(title__icontains=query) | Q(kr_op__icontains=query)
        )
        return object_list


class SearchResultsView8(ListView):
    model = NPA_SZZ
    template_name = 'reestr/search/search_results8.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = NPA_SZZ.objects.filter(
            Q(title__icontains=query) | Q(kr_op__icontains=query)
        )
        return object_list

class SearchResultsView9(ListView):
    model = NPA_GOSREG
    template_name = 'reestr/search/search_results9.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = NPA_GOSREG.objects.filter(
            Q(title__icontains=query) | Q(kr_op__icontains=query)
        )
        return object_list

class SearchResultsView10(ListView):
    model = NPA_LICENZ
    template_name = 'reestr/search/search_results10.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = NPA_LICENZ.objects.filter(
            Q(title__icontains=query) | Q(kr_op__icontains=query)
        )
        return object_list

class SearchResultsView11(ListView):
    model = OPT_STAND
    template_name = 'reestr/search/search_results11.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = OPT_STAND.objects.filter(
            Q(title__icontains=query) | Q(kr_op__icontains=query)
        )
        return object_list

class SearchResultsView12(ListView):
    model = ADM_REG
    template_name = 'reestr/search/search_results12.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = ADM_REG.objects.filter(
            Q(title__icontains=query) | Q(kr_op__icontains=query)
        )
        return object_list