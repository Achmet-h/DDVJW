"""
Django settings for DDVJW project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "dfjnghjzxdfngkdxfnrgjdrgiu+yunf$w__-8%lvmn6ucict_a1u=2u8o9"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'email'
EMAIL_HOST_PASSWORD = 'password'



ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "ckeditor",
    "jazzmin",
    "snowebsvg",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_bootstrap5",
    "content_app",
    "users"
]

JAZZMIN_SETTINGS = {
    "site_title": "Trainer Panel",
    "site_header": "Adminstratie",
    "site_logo": "content_app/Logo_DDVJW_splitted.png",
    "login_logo": "content_app/Logo_DDVJW_splitted.png",
    "site_icon": "content_app/favicon-32x32.png",
    "welcome_sign": "Welkom naar de Trainer Dashboard",
    "default_theme": "slate",
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]}
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "show_ui_builder": False,
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "content_app.Content": "fas fa-photo-video",
        "content_app.faq": "fas fa-comments",
        "users.User": "fas fa-user-circle",
    },
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "DDVJW.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "content_app/templates/content_app"),
                 os.path.join(BASE_DIR, "users/templates/users")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "DDVJW.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# using custom user model
AUTH_USER_MODEL = 'users.User'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }

    # "default": {
    #     "ENGINE": "django.db.backends.mysql",
    #     "NAME": "ddvjw_db",
    #     "USER": "root",
    #     "PASSWORD": "4206",
    #     "HOST": "127.0.0.1",
    #     "PORT": "3306"
    # }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Use https for the site instead of http
SECURE_SSL_REDIRECT = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_ROOT = [
    BASE_DIR / '/content_app/static'
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'content_app/static/content_app/media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
