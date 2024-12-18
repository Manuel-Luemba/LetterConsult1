"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os.path
from pathlib import Path
from app import db
import core

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v=dx$&uzta#4f=c10+m3q3t^x=51q(%*vf2zduad&cu+=x=j57'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',

    'core.erp',
    'core.homepage',
    'core.login',
    'core.user',
    'core.reports',
    'ckeditor',
    'ckeditor_uploader',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'crum.CurrentRequestUserMiddleware'
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
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

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = db.SQLITE

# Password validation
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

LANGUAGE_CODE = 'pt-pt'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
STATIC_ROOT = os.path.join(BASE_DIR, '/staticfiles/')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

LOGIN_REDIRECT_URL = '/erp/dashboard/'

LOGOUT_REDIRECT_URL = '/login/'

LOGIN_URL = '/login/'

AUTH_USER_MODEL = 'user.User'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.engconsult-ao.com'  # Servidor SMTP
EMAIL_PORT = 587  # Porta TLS para o Gmail
EMAIL_USE_TLS = True  # Use TLS
EMAIL_HOST_USER = 'engconsult.reports@engconsult-ao.com'  # Seu endereço de e-mail
EMAIL_HOST_PASSWORD = 'Reports#2024'  # Sua senha de e-mail
DEFAULT_FROM_EMAIL = 'engconsult.reports@engconsult-ao.com'
EMAIL_TIMEOUT = 60  # Em segundos

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'
#
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',  # Use 'Basic' para uma barra de ferramentas simplificada
        'extraPlugins': 'autogrow',  # Adiciona o plugin autogrow
        'autoGrow_minHeight': 300,  # Altura mínima do editor
        'autoGrow_maxHeight': 1200,  # Altura máxima do editor
        'autoGrow_bottomSpace': 50,  # Espaço embaixo quando o editor crescer
        'removePlugins': 'resize',  # Remove o redimensionamento manual (opcional)
        'extraPlugins': 'font',  # Certifique-se de que o plugin 'font' está ativado
        'font_names': 'Gill Sans MT/Gill Sans MT;Arial/Arial;Times New Roman/Times New Roman;',
        # Adicione 'Gill Sans MT' às opções de fontes
        'height': 400,
        'width': '100%',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['Image', 'Table', 'HorizontalRule', 'SpecialChar'],
            ['Undo', 'Redo'],
            ['Source'],
            ['Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Maximize', 'ShowBlocks', 'RemoveFormat']
        ],
        'extraPlugins': ','.join([
            'div',  # Plugin para criação de divisões de conteúdo
            'codesnippet',  # Plugin para adicionar snippets de código
            'widget',  # Adiciona widgets customizáveis
            'lineutils',
        ]),
        'filebrowserBrowseUrl': '/browse/',  # URL para navegar pelos arquivos
    },
}

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
