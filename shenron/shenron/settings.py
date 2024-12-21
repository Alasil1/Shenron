"""
Django settings for shenron project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import mysql.connector
import os

from plyer import notification

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_FROM = 's-omar_yasser@zewailcity.edu.eg'
EMAIL_HOST_USER = 's-omar_yasser@zewailcity.edu.eg'
EMAIL_HOST_PASSWORD = 'xgln nble lnep tuuk'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
PASSWORD_RESET_TIMEOUT = 600

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-&)=v+fh8&*@+b&k3cy&#1xl+-i-g(w6!q23x$z$20#@v&rs#v$"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# SESSION_CACHE_ALIAS = 'default'

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }
ALLOWED_HOSTS = [
    'uaenorth-01.azurewebsites.net',        # Root domain
    '.uaenorth-01.azurewebsites.net',
    'shenron-brfqhncsc4fmb6bu.uaenorth-01.azurewebsites.net'       # All subdomains (leading dot)
    '127.0.0.1',
    'localhost',
    '*'
]

SITE_ID=1
# Application definition
# Add this line to specify the custom user model
AUTH_USER_MODEL = 'user.User'
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'user',
    'UserProfile',
    'review',
    'MoviePage',
    'rest_framework',
    'forum',
    'favourite_list',
    'search',
    'admin_moderator',
    'tokens',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'notifications'
]
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        "AUTH_PARAMS":{'access_type':'online'},
}
}
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # 'django.middleware.messages',
    "allauth.account.middleware.AccountMiddleware"
]
# settings.py

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ROOT_URLCONF = "shenron.urls"
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "shenron.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# cloud
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "shenron",
        "USER": "Alasil",
        "PASSWORD": "a_12:14B%9",
        "HOST": "shenron.mysql.database.azure.com",
        "PORT": "3306",
        'OPTIONS': {
            'ssl': {'ca': '/app/DigiCertGlobalRootCA.crt.pem'
            },
        }
    }
}

# local
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": "movies",
#         "USER": "root",
#         "PASSWORD": "omar3322",
#         "HOST": "localhost",
#         "PORT": "3306",
#         # 'OPTIONS': {
#         #     'ssl': {'ca': '/app/DigiCertGlobalRootCA.crt.pem'
#         #     },
#         }
#     }


CSRF_TRUSTED_ORIGINS = [
    'https://shenron-brfqhncsc4fmb6bu.uaenorth-01.azurewebsites.net',
    # Add other trusted origins if needed
]

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend","allauth.account.auth_backends.AuthenticationBackend",)

LOGIN_REDIRECT_URL='/shenron'
LOGOUT_REDIRECT_URL='/shenron'