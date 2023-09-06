"""
Django settings for health project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import environ
from pathlib import Path
from django.utils.translation import gettext_lazy as _


env = environ.Env(
    DEBUG=(bool),
    SECRET_KEY=(str),
    DATABASE_NAME=(str),
    DATABASE_USER=(str),
    DATABASE_PASSWORD=(str),
    DATABASE_HOST=(str),
    DATABASE_PORT=(str),
)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(BASE_DIR / '.env')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')  #'django-insecure-+xim15*%pj=#zww$1a9hfjnc(@^+enyi1(47!(otsm_u@!*3)v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = [
    '127.0.0.1',
    '192.168.1.249',
    '62.109.21.3',
    'alexey.kadeyshvili.fvds.ru',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'crispy_forms',
    'crispy_bootstrap5',
    'easy_select2',
    'rosetta',
    'main_page',
    'users',
    'patients',
    'dicts',
    'therapy',
    'surgery',
    'investment',
    'diagnosis',
    'reports',
    'resolution',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django_currentuser.middleware.ThreadLocalUserMiddleware',
]

ROOT_URLCONF = 'health.urls'

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

WSGI_APPLICATION = 'health.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

# if DEBUG:
#     AUTH_PASSWORD_VALIDATORS = [ ]
# else:
#     AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
#     ]

AUTH_PASSWORD_VALIDATORS = [ ]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = 'tk'

TIME_ZONE = 'Asia/Ashgabat'

USE_I18N = True
USE_I10N = True

USE_TZ = True

LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Русский'),
    ('tk', 'Türkmen'),
)

LANGUAGE_SESSION_KEY = 'session_django_language'
LANGUAGE_COOKIE_NAME = 'django_language'
DATA_LANGUAGE_COOKIE_NAME = 'data_language'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = '/home/asd/health/health_db/static_' #os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
    '192.168.1.249',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.AsdUser'

LOGIN_REDIRECT_URL = 'users:login'
LOGOUT_REDIRECT_URL = 'users:login'
LOGIN_URL = 'users:login'

LIST_PAGE_SIZE = 10

CRISPY_TEMPLATE_PACK = 'bootstrap5'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

SELECT2_JS = 'js/select2.js'
SELECT2_CSS = 'css/select2.css'

SELECT2_USE_BUNDLED_JQUERY = False
SELECT2_USE_BUNDLED_SELECT2 = True

USE_THOUSAND_SEPARATOR = True

DATE_INPUT_FORMATS = ('%d-%m-%Y')

PERIODS = (
        (-1, _('Выберите период')),
        (0, _('1 день')),
        (1, _('1 неделя')),
        (2, _('текущий месяц')),
        (3, _('текущий год')),
    )
