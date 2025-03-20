import os 
import json
import dj_database_url
from google.oauth2 import service_account
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default = 'qwertyuiop')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS =  [
    "pabloesteban-portfolio.up.railway.app",
    "127.0.0.1",
    "localhost",    
    ]

CSRF_TRUSTED_ORIGINS = [
    "http://pabloesteban-portfolio.up.railway.app",
    "https://pabloesteban-portfolio.up.railway.app",
    "https://pabloesteban-portfolio.up.railway.app/admin/login/?next=/admin/",

]

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Definición de aplicaciones instaladas
INSTALLED_APPS = [
    'projects.apps.PortfolioConfig',
    'core',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_ckeditor_5',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webpersonal.urls'

# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Agrega rutas de plantillas si las tienes
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

WSGI_APPLICATION = 'webpersonal.wsgi.application'

# Configuración de la base de datos (SQLite para desarrollo local)
DATABASES = {
   'default': dj_database_url.config(default=os.getenv("postgresql://postgres:gmxWOcdgAlAKfuBCNgroOFILFsOQwthT@postgres-uvtu.railway.internal:5432/railway", "sqlite:///db.sqlite3")),
    }

# Validadores de contraseña
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

# Internacionalización
LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
    STATICFILES_STORAGE ='whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# GOOGLE CLOUD
GOOGLE_CREDENTIALS = os.getenv('GOOGLE_CREDENTIALS')

if GOOGLE_CREDENTIALS:
    GOOGLE_CREDENTIALS = json.loads(GOOGLE_CREDENTIALS)  # Cargar JSON si existe
else:
    GOOGLE_CREDENTIALS = {}

# Configuración de Google Cloud Storage
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'mi-bucket-pabloesteban'

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'https://storage.googleapis.com/mi-bucket-pabloesteban/'