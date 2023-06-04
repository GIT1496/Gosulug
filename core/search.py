from SANZ_1.models import SEZItem, RESHItem, Reestr_2
from OTKAZ.models import OTKItem

from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
class SearchResultsView(ListView):
    model = SEZItem
    template_name = 'reestr/search/search_results.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = SEZItem.objects.filter(
             Q(SEZ__Nomer__icontains=query) | Q(product__namber__icontains=query) | Q(product__predpr__icontains=query)
        )
        return object_list


class SearchResultsView1(ListView):
    model = OTKItem
    template_name = 'reestr/search/search_results1.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = OTKItem.objects.filter(
             Q(otk__Nomer1__icontains=query) | Q(product1__predpr__icontains=query)
        )
        return object_list


class SearchResultsView2(ListView):
    model = RESHItem
    template_name = 'reestr/search/search_results2.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = RESHItem.objects.filter(
             Q(resh__namber__icontains=query) | Q(sajav__Applicant__icontains=query) | Q(sajav__namber__icontains=query)
        )
        return object_list

class SearchResultsView3(ListView):
    model = Reestr_2
    template_name = 'reestr/search/search_results3.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = Reestr_2.objects.filter(
              Q(namber__exact=query)
        )
        return object_list


