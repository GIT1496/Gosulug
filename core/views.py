
from .models import Reestr_1, Reestr_2
from .util import Default_value
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SEZform, Reshform
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

# Сессия
from basket.forms import BasketAddProductForm
from django.views.generic import ListView

# Регистрация и авторизация
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, logout


# Форма обратной связи
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# API
from .serializers import Reestr1Serializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



def index_template(request):
    return render(request, 'reestr/index.html')


"""Отображение основной информации о заявлениях"""

# Вывод информации о внесенных заявлениях на государственные услуги
class SEZListView(PermissionRequiredMixin, SuccessMessageMixin, ListView, Default_value):  # Возврат листа объектов
    permission_required = 'core.add_reestr_1'
    login_url = 'user_login'
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


# Вывод детальной информации о СЭЗ
def SEZ_detail(request, SEZ):
    SEZ = Reestr_1.objects.get(pk=SEZ)
    form = BasketAddProductForm()
    return render(request, 'reestr/SEZ/SEZ-info.html', {'SEZ1_item': SEZ, 'form_basket': form})

# Метод для добавления СЭЗ
class SEZCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'core.add_reestr_1'
    login_url = 'user_login'
    model = Reestr_1
    form_class = SEZform   # Определение формы для взаимодействия
    template_name = 'reestr/SEZ/SEZ-add1.html'
    context_object_name = 'form'  # Переопределение ключа формы (object)
    success_message = 'Заявление на СЭЗ успешно зарегистрировано'
    success_url = reverse_lazy('list_SEZ_view')

# Метод для редактирования заявления на СЭЗ
class SEZUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'core.change_reestr_1'
    login_url = 'user_login'
    model = Reestr_1
    form_class = SEZform
    template_name = 'reestr/SEZ/SEZ-edit.html'
    context_object_name = 'form'
    success_message ='Заявление на СЭЗ успешно изменено'
    success_url = reverse_lazy('list_SEZ_view')

# Вывод информации о внесенных заявлениях на СЗЗ
class ReshenieView(PermissionRequiredMixin, SuccessMessageMixin, ListView):
    permission_required = 'core.add_reestr_2'
    login_url = 'user_login'
    model = Reestr_2
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

# Создания заявления на СЗЗ
class RESHCreateView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'core.add_reestr_2'
    login_url = 'user_login'
    model = Reestr_2
    form_class = Reshform  # Определение формы для взаимодействия
    template_name = 'reestr/Reshen/Resh_add1.html'
    context_object_name = 'form'  # Переопределение ключа формы (object)
    success_message = 'Заявление на Решение успешно добавлено'
    success_url = reverse_lazy('list_RESH_view')

# Редактирование заявления на СЗЗ
class RESHUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'core.change_reestr_2'
    login_url = 'user_login'
    model = Reestr_2
    form_class = Reshform
    template_name = 'reestr/Reshen/RESH-edit.html'
    context_object_name = 'form'
    success_message = 'Заявление на Решение успешно изменено'
    success_url = reverse_lazy('list_RESH_view')

# Вывод детальной информации о заявлении на СЗЗ
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

# Форма обратной связи
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
            login(request, user)
            messages.success(request, 'Вы успешно авторизовались')
            return redirect('list_SEZ_view')
        messages.error(request, 'Авторизация прошла с ошибкой, перепроверьте логин и/или пароль')
    else:
        form = LoginForm()
    return render(request, 'reestr/auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


# Вывод ошибок
def error_404(request, exception):
    context = dict()
    context['title'] = 'Упс, вы попали куда-то не туда'
    response = render(request, 'reestr/error/404.html')
    response.status_code = 404
    return response

def error_400(request, exception):
    context = dict()
    context['title'] = 'неправильный, некорректный запрос'
    response = render(request, 'reestr/error/400.html')
    response.status_code = 400
    return response

def error_403(request, exception):
    context = dict()
    context['title'] = 'запрещено (не уполномочен)'
    response = render(request, 'reestr/error/403.html')
    response.status_code = 403
    return response

def error_500(request, exception):
    context = dict()
    context['title'] = 'внутренняя ошибка сервера'
    response = render(request, 'reestr/error/500.html')
    response.status_code = 500
    return response



# Миксины для прав пользователей

class SEZADD(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'core.add_reestr_1'
    login_url = 'user_login'
    model = Reestr_1
    form_class = SEZform  # Определение формы для взаимодействия
    template_name = 'reestr/SEZ/SEZ-add1.html'
    context_object_name = 'form'  # Переопределение ключа формы (object)
    success_message = 'Заявление на СЭЗ успешно зарегистрировано'
    success_url = reverse_lazy('list_SEZ_view')

class SEZEDIT (PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'core.change_reestr_1'
    login_url = 'user_login'
    model = Reestr_1
    form_class = SEZform
    template_name = 'reestr/SEZ/SEZ-edit.html'
    context_object_name = 'form'
    success_message ='Заявление на СЭЗ успешно изменено'
    success_url = reverse_lazy('list_SEZ_view')

class SEZVIEW (PermissionRequiredMixin, SuccessMessageMixin, ListView):
    permission_required = 'core.add_reestr_1'
    login_url = 'user_login'
    model = Reestr_1 # определение таблицы для взаимодействия
    template_name = 'reestr/SEZ/SEZ-list.html'  # путь шаблона (<Имя приложения>/<Имя модели>_list.html)
    context_object_name = 'Reestr_1'  # Отправка данных по заданному ключу (object_list)
    queryset = Reestr_1.objects.filter(Vip=False)
    extra_context = {'title': 'Список заявлений на санитарно-эпидемиологические заключения'}  # Доп. значения (статичные данные)

class RESHADD(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'core.add_reestr_2'
    login_url = 'user_login'
    model = Reestr_2
    form_class = Reshform  # Определение формы для взаимодействия
    template_name = 'reestr/Reshen/Resh-list.html'
    context_object_name = 'form'  # Переопределение ключа формы (object)
    success_message = 'Заявление на Решение успешно зарегистрировано'
    success_url = reverse_lazy('list_RESH_view')

class RESHEDIT(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'core.change_reestr_2'
    login_url = 'user_login'
    model = Reestr_2
    form_class = Reshform
    template_name = 'reestr/Reshen/RESH-edit.html'
    context_object_name = 'form'
    success_message = 'Заявление на Решение успешно изменено'
    success_url = reverse_lazy('list_RESH_view')

class RESHVIEW (PermissionRequiredMixin, SuccessMessageMixin, ListView):
    permission_required = 'core.add_reestr_2'
    login_url = 'user_login'
    model = Reestr_2 # определение таблицы для взаимодействия
    template_name = 'reestr/Reshen/Resh-list.html'  # путь шаблона (<Имя приложения>/<Имя модели>_list.html)
    context_object_name = 'Reestr_2'  # Отправка данных по заданному ключу (object_list)
    queryset = Reestr_1.objects.filter(Vip=False)
    extra_context = {'title': 'Список заявлений на санитарно-эпидемиологические заключения'}  # Доп. значения (статичные данные)

# API заявлений
@api_view(['GET'])
def reestr_api_list_SEZ(request, format=None):
    if request.method == "GET":
        reestr = Reestr_1.objects.all()
        serializer = Reestr1Serializer(reestr, many=True)
        return Response({'reestr_list': serializer.data})

@api_view(['GET'])
def reestr_api_list_RESH(request, format=None):
    if request.method == "GET":
        reestr = Reestr_1.objects.all()
        serializer = Reestr1Serializer(reestr, many=True)
        return Response({'reestr_list': serializer.data})



