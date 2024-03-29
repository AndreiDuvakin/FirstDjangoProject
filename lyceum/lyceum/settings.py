import os
from pathlib import Path

from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

LANGUAGES = [
    ("en", _("Английский")),
    ("ru", _("Русский")),
]

USE_I18N = True

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", default="google")

DEBUG = os.environ.get("DJANGO_DEBUG", default="false")
DEBUG = DEBUG.lower().strip() in ("true", "yes", "1", "y", "t")

ALLOW_REVERSE = os.environ.get("DJANGO_ALLOW_REVERSE", default="true")
ALLOW_REVERSE = ALLOW_REVERSE.lower().strip() in (
    "true",
    "yes",
    "1",
    "y",
    "t",
)

DEFAULT_USER_IS_ACTIVE = os.getenv(
    "DEFAULT_USER_IS_ACTIVE",
    default=str(DEBUG),
).lower() in [
    "true",
    "1",
    "yes",
    "y",
]

AUTH_USER_MODEL = "auth.User"

DJANGO_MAIL = os.environ.get(
    "DJANGO_MAIL",
)

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", default="*").split(",")

INSTALLED_APPS = [
    "about.apps.AboutConfig",
    "catalog.apps.CatalogConfig",
    "homepage.apps.HomepageConfig",
    "download.apps.DownloadConfig",
    "feedback.apps.FeedbackConfig",
    "core.apps.CoreConfig",
    "users.apps.UsersConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "sorl.thumbnail",
    "ckeditor",
    "django_cleanup.apps.CleanupConfig",
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

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"

EMAIL_FILE_PATH = BASE_DIR / "send_mail"

LOGIN_URL = "/users/login/"

LOGIN_REDIRECT_URL = "/"

LOGOUT_REDIRECT_URL = "/users/login/"
