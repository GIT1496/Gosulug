"""
Django settings for Gosulug project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

"""Настройки проекта"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o=#2of&@j==i4pl^*5%ls1%&5v)g43nmr7hujfew-91@45p=u^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost',
                 '127.0.0.1']


# Установленны приложения в проекте

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'widget_tweaks',
    "basket",
    'dashboardgosusl',
    'controlcenter',
    "KMS_sotr",
    'SANZ_1',
    "OTKAZ",
    'coverage',
    "rest_framework",
    'rangefilter',
    'multiselectfield',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Gosulug.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Gosulug.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Rospotreb',
        'USER': 'postgres',
        'PASSWORD': 'QE5789oiplGH+',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Настройка проверки пароля
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

import os
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR/'static')

import os
STATICFILES_DIRS = [
os.path.join(BASE_DIR, 'core/static'),
os.path.join(BASE_DIR, 'Gosulug/static'),
os.path.join(BASE_DIR, 'OTKAZ/static'),
os.path.join(BASE_DIR, 'SANZ_1/static'),
]



# Путь для медиаконтента

import os

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Установка пути для медиа-контента
MEDIA_URL = '/media/'  # URL-адрес для контента


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Session
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
# SESSION_COOKIE_AGE = 1209600
# SESSION_COOKIE_SECURE = True
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_SAVE_EVERY_REQUEST = True
BASKET_SESSION_ID = 'basket'


EMAIL_HOST = 'smtp.mail.ru'  # Сервер для отправки писем
EMAIL_PORT = 465  # Порт сервера SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = 'mikhail_m_bulanov_bulanov@mail.ru'  # Логин пользователя
EMAIL_HOST_PASSWORD = 'Qf8HJKFy2BnxYXQXiML9'  # Пароль для внешнего приложения из электронного ящика
EMAIL_USE_TLS_TLS = False  # Протокол шифрования TLS
EMAIL_USE_SSL = True


# Настройки REST_FRAMEWORK
REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': [
    # ]
}

