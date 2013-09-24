# Django settings for risiti project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
user = os.environ['RISITI_USER']
password = os.environ['RISITI_PASSWORD']

#admins = (
#    ('', ''),
#)

#managers = admins

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'risiti',                      # or path to database file if using sqlite3.
        # the following settings are not used with sqlite3:
        'USER': user,
        'PASSWORD': password,
        'HOST': 'localhost',                      # empty for localhost through domain sockets or '127.0.0.1' for localhost through tcp.
        'PORT': '5432',                      # set to empty string for default.
    }
}

# hosts/domain names that are valid for this site; required if debug is false
# see https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# local time zone for this installation. choices can be found here:
# http://en.wikipedia.org/wiki/list_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# in a windows environment this must be set to your system time zone.
TIME_ZONE = 'Africa/Nairobi'

# language code for this installation. all choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-ke'

SITE_ID = 1

# if you set this to false, django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# if you set this to false, django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# if you set this to false, django will not use timezone-aware datetimes.
USE_TZ = True

# absolute filesystem path to the directory that will hold user-uploaded files.
# example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# url that handles the media served from media_root. make sure to use a
# trailing slash.
# examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# absolute path to the directory static files should be collected to.
# don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in staticfiles_dirs.
# example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# url prefix for static files.
# example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# additional locations of static files
STATICFILES_DIRS = (
    # put strings here, like "/home/html/static" or "c:/www/django/static".
    # always use forward slashes, even on windows.
    # don't forget to use absolute paths, not relative paths.
)

# list of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.filesystemfinder',
    'django.contrib.staticfiles.finders.appdirectoriesfinder',
#    'django.contrib.staticfiles.finders.defaultstoragefinder',
)

# make this unique, and don't share it with anybody.
SECRET_KEY = 'v1luw=i@mx(74le-hpx6u8bzsc@weqr)h-^ql-f5$hf8maqz6k'

# list of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.loader',
    'django.template.loaders.app_directories.loader',
#     'django.template.loaders.eggs.loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.commonmiddleware',
    'django.contrib.sessions.middleware.sessionmiddleware',
    'django.middleware.csrf.csrfviewmiddleware',
    'django.contrib.auth.middleware.authenticationmiddleware',
    'django.contrib.messages.middleware.messagemiddleware',
    # uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.xframeoptionsmiddleware',
)

ROOT_URLCONF = 'risiti.urls'

# python dotted path to the wsgi application used by django's runserver.
WSGI_APPLICATION = 'risiti.wsgi.application'

TEMPLATE_DIRS = (
    # put strings here, like "/home/html/django_templates" or "c:/www/django/templates".
    # always use forward slashes, even on windows.
    # don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # uncomment the next line to enable the admin:
    'django.contrib.admin',
    # uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# a sample logging configuration. the only tangible logging
# performed by this configuration is to send an email to
# the site admins on every http 500 error when debug=false.
# see http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
