from .base import BASE_DIR

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%3p5e103wby!yyao5zd2^%)gavi_ekw9a*cvf@84elifhqsnu='

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "cattlecam_admin",
        "PASSWORD": "cattlecam_pwd",
        "HOST": "cattelcam.cepknzg1ajty.eu-central-1.rds.amazonaws.com",
        "PORT": 5432
    }
}
