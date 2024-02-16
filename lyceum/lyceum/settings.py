import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", default="google")

DEBUG = os.environ.get("DJANGO_DEBUG", default="false").lower().strip() in (
    "true",
    "yes",
    "1",
    "y",
    "t",
)

ALLOW_REVERSE = os.environ.get(
    "DJANGO_ALLOW_REVERSE", default="true"
).lower().strip() in (
    "true",
    "yes",
    "1",
    "y",
    "t",
)

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", default="*").split(",")

INSTALLED_APPS = [
    "about.apps.AboutConfig",
    "catalog.apps.CatalogConfig",
    "homepage.apps.HomepageConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "lyceum.middleware.FlipWordMiddleware",
]

if DEBUG:
    INSTALLED_APPS += [
        "debug_toolbar",
    ]
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

ROOT_URLCONF = "lyceum.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

INTERNAL_IPS = ["127.0.0.1", "localhost", "*"]

WSGI_APPLICATION = "lyceum.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth."
        "password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib."
        "auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib."
        "auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib."
        "auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
