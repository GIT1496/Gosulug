from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Reestr_1, Reestr_2
from OTKAZ.models import OTKItem
from .util import Default_value
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SEZform, Reshform
from basket.forms import BasketAddProductForm
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from SANZ_1.models import SEZItem
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator


from django.contrib import messages

from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
# API
from .serializers import Reestr1Serializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets

from django.core.paginator import Paginator


def index_template(request):
    return render(request, 'reestr/index.html')


# def reestr_template(request):
#     context = {'title': 'Заявления'}
#
#     reestr = Reestr_1.objects.all
#     context['reestr_list'] = reestr
#
#     # Paginator
#     paginator = Paginator(reestr, 1)  # Создаем пагинатор из списка фруктов и делаем страницы по 3 элемента
#     page_num = request.GET.get('page', 1)  # Получение страницы, на которой находится наш пользователь
#     page_objects = paginator.get_page(page_num)  # Получение группы элементов(3) по номеру страницы
#     context['page_obj'] = page_objects  # Передача данных на .html
#
#     print(page_objects.object_list)
#     # context = {
#     #     'title': 'Фрукты',
#     #     'fruit_list': fruits,
#     #     'fruit_one': fruit_one,
#     #     'name': name
#     # }
#     return render(
#         request=request,
#         template_name='reestr/SEZ/SEZ-list.html',
#         context=context
#     )
class SEZListView(ListView, Default_value):  # Возврат листа объектов
    model = Reestr_1 # определение таблицы для взаимодействия
    template_name = 'reestr/SEZ/SEZ-list.html'  # путь шаблона (<Имя приложения>/<Имя модели>_list.html)
    context_object_name = 'Reestr_1'  # Отправка данных по заданному ключу (object_list)
    queryset = Reestr_1.objects.filter(Vip=False)
    extra_context = {'title': 'Список заявлений на санитарно-эпидемиологические заключения'}  # Доп. значения (статичные данные)

    def get_context_data(self, *args, **kwargs):
        wiki_list = Reestr_1.objects.order_by('namber')
        context = super(SEZListView, self).get_context_data(*args, **kwargs)
        context["wiki_list"] = wiki_list
        return context

    paginate_by = 5


def SEZ_detail(request, SEZ):
    SEZ = Reestr_1.objects.get(pk=SEZ)
    form = BasketAddProductForm()
    return render(request, 'reestr/SEZ/SEZ-info.html', {'SEZ1_item': SEZ, 'form_basket': form})



# def SEZ_form(request):
#     if request.method == "POST":
#         form = SezOkForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#
#             Reestr_1.objects.create(
#                 Nomer = form.cleaned_data["Nomer"],
#                 tipogr=form.cleaned_data['tipogr'],
#             )
#             # ==
#             # Supplier.objects.create(
#             #     **form.cleaned_data
#             # )
#             # return HttpResponseRedirect('/fruit/supplier/add/') # в методе указ. URL-адрес
#
#             return redirect('list_supp')  # В методе указывается URL-адрес, название пути, модель
#         else:
#             context = {'form': form}
#             return render(request, 'reestr/SEZ/SEZ-edit.html', context)
#     else:
#         form = SezOkForm()
#         context = {'form': form}
#         return render(request, 'reestr/SEZ/SEZ-edit.html', context)



class SEZCreateView(CreateView):
    model = Reestr_1
    form_class = SEZform   # Определение формы для взаимодействия
    template_name = 'reestr/SEZ/SEZ-add1.html'
    context_object_name = 'form'  # Переопределение ключа формы (object)
    success_url = reverse_lazy('list_SEZ_view')


    @method_decorator(permission_required('core.add_Reestr_1'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



class SEZUpdateView(UpdateView):
    model = Reestr_1
    form_class = SEZform
    template_name = 'reestr/SEZ/SEZ-edit.html'
    context_object_name = 'form'
    success_url = reverse_lazy('list_SEZ_view')



class ReshenieView(ListView):
    model = Reestr_2
    form_class = SEZform
    template_name = 'reestr/Reshen/Resh-list.html'  # путь шаблона (<Имя приложения>/<Имя модели>_list.html)
    context_object_name = 'Reestr_2'  # Отправка данных по заданному ключу (object_list)
    queryset = Reestr_2.objects.filter(Vip=False)
    extra_context = {
        'title': 'Список заявлений на решения'}  # Доп. значения (статичные данные)

    def get_context_data(self, *args, **kwargs):
        wiki_list = Reestr_2.objects.order_by('namber')
        context = super(ReshenieView, self).get_context_data(*args, **kwargs)
        context["wiki_list"] = wiki_list
        return context

    paginate_by = 5


class RESHCreateView(CreateView):
    model = Reestr_2
    form_class = Reshform  # Определение формы для взаимодействия
    template_name = 'reestr/Reshen/Resh_add1.html'
    context_object_name = 'form'  # Переопределение ключа формы (object)
    success_url = reverse_lazy('list_RESH_view')

class RESHUpdateView(UpdateView):
    model = Reestr_2
    form_class = Reshform
    template_name = 'reestr/Reshen/RESH-edit.html'
    context_object_name = 'form'
    success_url = reverse_lazy('list_RESH_view')

def resh_detail(request, RES1):
    RES1 = Reestr_2.objects.get(pk=RES1)
    form = BasketAddProductForm()
    return render(request, 'reestr/Reshen/RESH-info.html', {'RES1_item': RES1, 'form_basket': form})


# регистрация
def user_registration(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST) # Форма создания пользователя из auth
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Запись нового пользователя
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Не удалось зарегистрировать')
    else:
        # form = UserCreationForm()
        form = RegistrationForm()
    return render(request, 'reestr/auth/registration.html', {'form': form})

#email
def send_contact_email(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            mail = send_mail(  # Отправка письма
                form.cleaned_data['subject'],  # Заголовок письма
                form.cleaned_data['content'],  # Тело письма
                settings.EMAIL_HOST_USER,  # Отправитель письмо
                (['django1496@mail.ru']),
                fail_silently=True,  # Режим отображения ошибок (True - исключения не будет)
                #                               (False - исключения выведутся на страницу)
            )
            if mail:
                messages.success(request, 'Письмо было успешно отправлено')
                return redirect('list_SANZ_view')
            else:
                messages.error(request, 'Письмо не удалось успешно отправить')
        else:
            messages.error(request, 'Письмо заполнено неверно')
    else:
        form = ContactForm()
    return render(request, 'reestr/other/contact.html', {'title': 'Вопросы', 'form': form})






#Авторизация
def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user)
            print(request.user.is_authenticated)
            print(request.user.is_anonymous)
            login(request, user)
            print(request.user.is_authenticated)
            print(request.user.is_anonymous)
            messages.success(request, 'Вы успешно авторизовались')
            return redirect('list_SEZ_view')
        messages.error(request, 'Авторизация прошла с ошибкой, перепроверьте логин и/или пароль')
    else:
        form = LoginForm()
    return render(request, 'reestr/auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')

# Права пользователя
def is_login(request):
    if request.user.is_anonymous:
        return HttpResponse('<h1>Вы аноним</h1>')
    else:
        return HttpResponse('<h1>Зарегистрированы</h1>')


@login_required
def is_login_decorator(request):
    return HttpResponse('<h1>Зарегистрированы</h1>')


def is_permession(request):
    text = ''
    if request.user.has_perm('Boormag.add_Library'):  # <Название приложения>.<операция>_<название модели>
        text += '<h1>Вы можете добавлять книги</h1>'
    if request.user.has_perm('Boormag.change_Library'):
        text += '<h1>Вы можете изменять книги</h1>'
    if request.user.has_perm('Boormag.view_Library'):
        text += '<h1>Вы можете просматривать книги</h1>'
    if text == '':
        HttpResponse('<h1>У вас нет прав</h1>')
    return HttpResponse(text)


@permission_required('Boormag.add_Library')
def is_perm_add(request):
    return HttpResponse('<h1>Добавление книги</h1>')


@permission_required('Boormag.change_Library')
def is_perm_change(request):
    return HttpResponse('<h1>Изменение книг</h1>')


@permission_required(['Boormag.change_supplier', 'Boormag.view_Library'])
def is_perm_change_view(request):
    return HttpResponse('<h1>Изменение и просмотр книг</h1>')

# Вывод ошибок
def error_404(request, exception):
    context = dict()
    context['title'] = 'Упс, вы попали куда-то не туда'
    response = render(request, 'library/error/404.html')
    response.status_code = 404
    return response

def error_400(request, exception):
    context = dict()
    context['title'] = 'неправильный, некорректный запрос'
    response = render(request, 'library/error/400.html')
    response.status_code = 400
    return response

def error_403(request, exception):
    context = dict()
    context['title'] = 'запрещено (не уполномочен)'
    response = render(request, 'library/error/403.html')
    response.status_code = 403
    return response

def error_500(request, exception):
    context = dict()
    context['title'] = 'внутренняя ошибка сервера'
    response = render(request, 'library/error/500.html')
    response.status_code = 500
    return response


# API заявлений
@api_view(['GET', 'POST'])
def reestr_api_list(request, format=None):
    if request.method == "GET":
        reestr = Reestr_1.objects.all()
        serializer = Reestr1Serializer(reestr, many=True)
        return Response({'reestr_list': serializer.data})
        # return JsonResponse({'fruits_list': serializer.data})
        # return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        serializer = Reestr1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def reestr_api_detail(request, pk, format=None):
    reestr_obj = get_object_or_404(Reestr_1)


    if request.method == 'GET':
        serializer = Reestr1Serializer(reestr_obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Reestr1Serializer(reestr_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        reestr_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



