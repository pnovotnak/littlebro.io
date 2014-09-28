RATING_STAR_WIDTH = 13.5

SITE_ID = 1

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'littlebro.io',
    'executive.littlebro.io',
    'legislative.littlebro.io',
    'judicial.littlebro.io',
]


CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Advanced',
        'width': 1000,
        'height': 600,
    },
}

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

# Application definition

INSTALLED_APPS = (
    'grappelli', # Keep this here
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    # 3rd party
    'captcha',
    'ckeditor',

    'littlebro',
    'recaptcha',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
]

ROOT_URLCONF = 'littlebro.urls'

WSGI_APPLICATION = 'littlebro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media files (Uploads)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

RECAPTCHA_USE_SSL = True
RECAPTCHA_PUBLIC_KEY = '6LeIDPsSAAAAAB7v6kh3b9TXWTnWB7ESlrgtSf7u'
RECAPTCHA_PRIVATE_KEY = '6LeIDPsSAAAAACYSU0rjXY36fjiiNMHNVjZaO42o'

try:
    SECRET_KEY
except NameError:
    SECRET_FILE = os.path.join(BASE_DIR, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            import random
            SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters \
            to generate your secret key!' % SECRET_FILE)


try:
    from base_local import *
except ImportError:
    pass
