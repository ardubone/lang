import os
from pathlib import Path
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))
# BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', None)

DEBUG = False

CORS_ALLOW_CREDENTIALS = True
CORS_REPLACE_HTTPS_REFERER = True
CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = [
    'http://TalkAboutAll.pythonanywhere.com',
    "http://localhost:3000",
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://193.168.49.66:44444',
    "https://rugutosas.beget.app",
    "http://localhost:44444",
    "https://localhost:44444",
    "http://localhost:8000",
    "https://localhost:8000",
    "http://0.0.0.0:8000",
    "https://talkaboutall.store"

]

ALLOWED_HOSTS = [
    '*'
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ORIGIN_WHITELIST = (
    'http://TalkAboutAll.pythonanywhere.com',
    "http://localhost:3000",
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://193.168.49.66:44444',
    "https://rugutosas.beget.app",
    "http://localhost:44444",
    "https://localhost:44444",
    "http://0.0.0.0:8000",
    "https://talkaboutall.store"
)

SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO", os.environ.get('HTTP_X_FORWARDED_PROTO', "http")
)
SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', False)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    'djoser',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'storages',
    'drf_spectacular',
    'django_celery_results',
    'django_celery_beat',

    'talk_core.apps.TalkCoreConfig',
    'record.apps.RecordConfig',
    'theme.apps.ThemeConfig',
    'users.apps.UsersConfig',
]

AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12,
    'DEFAULT_SCHEMA_CLASS': 'api.views.CustomAutoSchema',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',)
}

DJOSER = {
    'LOGIN_FIELD': 'email',
    'PASSWORD_RESET_CONFIRM_URL': '',
    'ACTIVATION_URL': 'api/auth/activate/{uid}/{token}/',
    'SEND_ACTIVATION_EMAIL': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': False,
    'USER_CREATE_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,
    'SERIALIZERS': {
        'user_create': 'users.serializers.CustomUserCreateSerializer',
    },
    'PERMISSIONS': {
        'user': ['rest_framework.permissions.AllowAny'],
    },
    'EMAIL': {
        'password_reset': 'users.email.CustomPasswordResetEmail'
    }
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=3),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('JWT',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE':
        'rest_framework_simplejwt.authentication.'
        'default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',
}

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

ROOT_URLCONF = 'talk_about_all.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            Path(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'talk_about_all.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', "talk_about_all"),
        'USER': os.environ.get('POSTGRES_USER', "root_db"),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST', "localhost"),
        'PORT': os.environ.get('POSTGRES_PORT', 5432),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
        'OPTIONS': {
            'user_attributes': (
                'email', 'first_name', 'last_name'
            ),
            'max_similarity': 1,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
    {
        'NAME': 'talk_core.validators.MaximumLengthValidator',
        'OPTIONS': {
            'max_length': 50,
        }
    },
    {
        'NAME': 'talk_core.validators.WhiteSpacesValidator',
    },
]

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SPECTACULAR_SETTINGS = {
    'TITLE': 'Talk about all',
    'DESCRIPTION': 'Upgrade your public speach to the next level',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    "ENABLE_USE_DEFAULT_RESPONSE": False,

}

# email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = os.environ.get('MEDIA_URL', '')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

UNSPLASH_TOKEN = os.environ.get('UNSPLASH_TOKEN', None)

# celery
CELERY_BROKER_URL = 'redis://localhost:6379'  # change to os.getenv()
CELERY_RESULT_BACKEND = 'django-db'  # change to os.getenv()
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_TIME_LIMIT = 30 * 60
CACHES = {
    'default': {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "redis://localhost:6379/1",
    }
}
CELERY_CACHE_BACKEND = 'default'

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
