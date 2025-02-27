import os
from pathlib import Path

# Construir rutas dentro del proyecto: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent

# CLAVE SECRETA (Solo para desarrollo local)
SECRET_KEY = 'qwertyuiop'

# DEBUG activado para desarrollo
DEBUG = True

# Hosts permitidos
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

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
]

# Definición del middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Para desarrollo local no es necesario usar whitenoise
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
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
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

# Archivos estáticos (CSS, JavaScript, Imágenes)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR / 'static'),
    ]

# Campo de clave primaria por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de archivos multimedia
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'