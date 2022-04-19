"""
Django settings for lawApp project.

Generated by 'django-admin startproject' using Django 2.2.20.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOST = 'https://direito-digital.herokuapp.com'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pfzw!70h-_4om^m0m)rkp9fp4(fsbd6n-st$*lxo%l8*prkm+*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'rest_framework',
    'rest_framework.authtoken',

    'dj_rest_auth',

    'customAdmin.apps.CustomadminConfig',
    'notes.apps.NotesConfig',
    'authentication.apps.AuthenticationConfig',
    'paypal.apps.PaypalConfig',
    'metrics.apps.MetricsConfig',
]

SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lawApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'lawApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'offline',
        }
    }
}

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]
STATIC_URL = '/static/'

ACCOUNT_AUTHENTICATION_METHOD = 'username'

CORS_ORIGIN_ALLOW_ALL = True

DEFAULT_RENDERER_CLASSES = ['rest_framework.renderers.JSONRenderer']

DEFAULT_AUTHENTICATION_CLASSES = [
    'rest_framework.authentication.TokenAuthentication',
    'django.contrib.auth.backends.ModelBackend'
]

if DEBUG:
    DEFAULT_RENDERER_CLASSES += ['rest_framework.renderers.BrowsableAPIRenderer']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': DEFAULT_AUTHENTICATION_CLASSES,
    'DEFAULT_RENDERER_CLASSES': DEFAULT_RENDERER_CLASSES,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_EMAIL_REQUIRED = True

# expressed in days
TRIAL_PERIOD = 60

# React Native Application
BUILD_VERSION_NAME = "3.0"
BUILD_VERSION_CODE = 9

PAYPAL_MODE = "live"
PAYPAL_CLIENT_ID = os.environ.get('PAYPAL_CLIENT_ID') if PAYPAL_MODE == "sandbox" else os.environ.get('PAYPAL_CLIENT_ID_LIVE')
PAYPAL_CLIENT_SECRET = os.environ.get('PAYPAL_CLIENT_SECRET') if PAYPAL_MODE == "sandbox" else os.environ.get('PAYPAL_CLIENT_SECRET_LIVE')
PAYPAL_3_MONTH_PLAN_ID = os.environ.get('PAYPAL_3_MONTH_PLAN_ID') if PAYPAL_MODE == "sandbox" else os.environ.get('PAYPAL_3_MONTH_PLAN_ID_LIVE')
PAYPAL_6_MONTH_PLAN_ID = os.environ.get('PAYPAL_6_MONTH_PLAN_ID') if PAYPAL_MODE == "sandbox" else os.environ.get('PAYPAL_6_MONTH_PLAN_ID_LIVE')
PAYPAL_12_MONTH_PLAN_ID = os.environ.get('PAYPAL_12_MONTH_PLAN_ID') if PAYPAL_MODE == "sandbox" else os.environ.get('PAYPAL_12_MONTH_PLAN_ID_LIVE')
PAYPAL_WEBHOOK_ID = os.environ.get('PAYPAL_WEBHOOK_ID') if PAYPAL_MODE == "sandbox" else os.environ.get('PAYPAL_WEBHOOK_ID_LIVE')
PAYPAL_PRODUCT_ID = "direito-digital-premium"


django_heroku.settings(locals())
