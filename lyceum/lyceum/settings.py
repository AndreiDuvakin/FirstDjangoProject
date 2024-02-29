import os
from pathlib import Path

from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

LANGUAGES = [
    ("en", _("English")),
    ("ru", _("Russian")),
]

USE_I18N = True

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", default="google")

DEBUG = os.environ.get("DJANGO_DEBUG", default="false").lower().strip() in (
    "true",
    "yes",
    "1",
    "y",
    "t",
)

ALLOW_REVERSE = os.environ.get(
    "DJANGO_ALLOW_REVERSE",
    default="true",
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
    "core.apps.CoreConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "sorl.thumbnail",
    "django_cleanup.apps.CleanupConfig",
    "ckeditor",
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
    "django.middleware.locale.LocaleMiddleware",
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
        "DIRS": [
            BASE_DIR / "templates",
        ],
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

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
    "*",
]

WSGI_APPLICATION = "lyceum.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
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

LANGUAGE_CODE = "ru"

LOCALE_PATHS = [
    BASE_DIR / "locale",
]

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static_dev",
]

MEDIA_ROOT = BASE_DIR / "media"

MEDIA_URL = "/media/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
