from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-^nvqpm4&4mz0!m-osoy=8c^8wvidw$majn4ge41+e2mtzxt+hn'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    
    'preventconcurrentlogins',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    
    
]

AUTH_USER_MODEL = 'app.User'

MIDDLEWARE = [
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'preventconcurrentlogins.middleware.PreventConcurrentLoginsMiddleware',
]


ROOT_URLCONF = 'datam.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'datam.wsgi.application'

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'data',
        'USER': 'postgres',
        'PASSWORD': 'Pass@123',
        # 'HOST': '13.234.208.246',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'

STATICFILES_DIRS = [

    os.path.join(BASE_DIR, "static") 

]

STATIC_ROOT = os.path.join(BASE_DIR,'assets') 

MEDIA_URL ='/media/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

SESSION_EXPIRE_AT_BROWSER_CLOSE = True