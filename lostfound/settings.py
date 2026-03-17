# lostfound/settings.py
# This settings file works for BOTH local development AND Render hosting

from pathlib import Path
import os
import dj_database_url

# ─── Base Directory ───────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ─── Secret Key ───────────────────────────────────────────────────
# Locally uses the default value
# On Render, it reads from the environment variable we set
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-local-dev-key-do-not-use-in-production'
)

# ─── Debug Mode ───────────────────────────────────────────────────
# True locally (shows errors), False on Render (hides errors)
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# ─── Allowed Hosts ────────────────────────────────────────────────
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.onrender.com',      # covers all *.onrender.com domains
]

# ─── Installed Apps ───────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',                # our main app
]

# ─── Middleware ───────────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # serves static files on Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lostfound.urls'

# ─── Templates ────────────────────────────────────────────────────
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
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lostfound.wsgi.application'

# ─── Database ─────────────────────────────────────────────────────
# If DATABASE_URL environment variable exists → use PostgreSQL (Render)
# Otherwise → use SQLite (local development)
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    # Production: PostgreSQL database on Render
    DATABASES = {
        'default': dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
        )
    }
else:
    # Local development: SQLite (simple file-based database)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ─── Password Validation ──────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ─── Internationalization ─────────────────────────────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# ─── Static Files ─────────────────────────────────────────────────
# WhiteNoise serves these files on Render
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ─── Media Files (user uploaded images) ──────────────────────────
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ─── Login Settings ───────────────────────────────────────────────
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/home/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'