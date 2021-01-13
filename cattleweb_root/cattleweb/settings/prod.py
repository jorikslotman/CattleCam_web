from .base import BASE_DIR
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "postgres",
#         "USER": os.environ['DB_USER'],
#         "PASSWORD": os.environ['DB_PWD'],
#         "HOST": os.environ['DB_HOST'],
#         "PORT": os.environ['DB_PORT']
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'database','db.sqlite3'),
    }
}

STATIC_ROOT = '/vol/cattleweb/static'
MEDIA_ROOT = '/vol/cattleweb/media'