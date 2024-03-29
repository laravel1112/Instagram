"""
Django settings for yoinable project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
from __future__ import absolute_import
from datetime import timedelta
import os
from celery.schedules import crontab
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_PARENT_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))
YOINABLE_APP_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "logs")

COREAPP = "instanalysis"
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(@3+y0xkqgh_)r*v6l*y$r0x7ombm*v_jc1n@-h488sg9o#e1&'
NEVERCACHE_KEY = 'a%3mbj-11%phqolxn=t=w9k3cx$$zlg2u6jxw0h%7ne%j3*4-4'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

MAIN_DOMAIN = "52.29.82.166"
WEB_URI = "http://%s" % MAIN_DOMAIN

ALLOWED_HOSTS = [MAIN_DOMAIN]
ADMINS = [('Eduardo Calleja', 'e.calleja.garcia@gmail.com')]
SERVER_EMAIL = 'admin@%s' % MAIN_DOMAIN
SEND_MAILS = True  # Disables all kind of email notifications
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django_super_popups',
    'widget_tweaks',
    'compressor',
    'instanalysis',
    'debug_toolbar'
]

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
)

ROOT_URLCONF = 'master.urls'

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
                'django.template.context_processors.media',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'master.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# TODO Change user for specific user for this application
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'instanalytics',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
    }
}


APPEND_SLASH = True

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ' [%(asctime)s] [%(levelname)s] [%(name)s] %(message)s'
        },
        'simple': {
            'format': ' %(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(LOG_PATH, '%s.log' % COREAPP)
        },
        'file_errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(LOG_PATH, '%s_errors.log' % COREAPP)
        },
        'file_worker': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(LOG_PATH, 'update_media.log')
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        }
    },
    'loggers': {
        '': {
            'handlers': ['file', 'file_errors', 'mail_admins'],
            'level': 'INFO'
        },
        'worker_publications': {
            'handlers': ['file_worker'],
            'level': 'DEBUG'
        },
        'django': {
            'handlers': ['file'],
            'level': 'INFO'
        }
    }
}


COMPRESS_ENABLED = False		
# Disabling online compression, we have to run python manage.py compress
COMPRESS_OFFLINE = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
COMPRESS_JS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'instanalysis/media')

FABRIC = {
    "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
    "SSH_USER": "instanalytics",  # VPS SSH username
    "HOSTS": ["52.29.82.166"],  # The IP address of your VPS
    "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
    "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
    "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
    # "DB_USER": DATABASES['default']['USER'],  # Live database user
    # "DB_PASS": DATABASES['default']['PASSWORD'],  # Live database password
    # "DB_NAME": DATABASES['default']['NAME'],   # Live database name
    "ADMIN_PASS": "admin",  # Live admin user password
    "SSH_KEY_PATH": None,  # define in local_settings.py
                           # set FABRIC['SSH_KEY_PATH'] = '~/path_to_file.pem'
    "REPOSITORY_REMOTE_URL": "https://github.com/invibeme/yoinable.git",
    "COMPRESS_OFFLINE": COMPRESS_OFFLINE,
    "SSL_DISABLED": False,
}
STATICFILES_PATH = "/home/%s/staticfiles/" % FABRIC['SSH_USER']
FABRIC['STATICFILES_PATH'] = STATICFILES_PATH
FABRIC['MEDIA_PATH'] = "/home/%s/instanalysis/instanalysis/media/" % FABRIC['SSH_USER']

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")
CACHE_MIDDLEWARE_SECONDS = 60
CACHE_MIDDLEWARE_KEY_PREFIX = COREAPP


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "127.0.0.1:11211",
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"

STATIC_ROOT = "/home/%s/staticfiles/" % FABRIC['SSH_USER']

TIME_ZONE = 'Europe/Madrid'

AWS_ACCESS_KEY_ID = 'AKIAJIUPNVBQOALYCYHA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_SES_REGION_ENDPOINT = 'email.eu-west-1.amazonaws.com'
EMAIL_BACKEND = 'django_ses.SESBackend'

######################
# INSTAGRAM SETTINGS #
######################

INSTAGRAM_CLIENT_ID = "0f726187bdb949cba308ca2864785eb2"
INSTAGRAM_SECRET_ID = "a4342089c479427eb213adfb4c7b5c43"

################
# CELERY STUFF #
################
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

CELERYBEAT_SCHEDULE = {
    'update_api_quotas': {
        'task': 'instanalysis.tasks.calculate_api_quotas',
        'schedule': crontab(minute='*')
    },
    'generate_file_categories': {
        'task': 'instanalysis.tasks.generate_categories_file',
        'schedule': crontab(hour=0, minute=0)
    },
    'reset_adhoc': {
        'task': 'instanalysis.tasks.reset_adhoc',
        'schedule': crontab(minute='0,30')
    },

}


# Allow any settings to be defined in local_settings.py which should be
# ignored in your version control system allowing for settings to be
# defined per machine.

# Instead of doing "from .local_settings import *", we use exec so that
# local_settings has full access to everything defined in this module.

f = os.path.join(YOINABLE_APP_PATH, "local_settings.py")
if os.path.exists(f):
    exec(open(f, "rb").read())
