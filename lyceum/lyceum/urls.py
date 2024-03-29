from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
import django.contrib.auth.urls
from django.urls import include, path
from django.views.i18n import set_language

urlpatterns = [
    path("", include("homepage.urls")),
    path("catalog/", include("catalog.urls")),
    path("about/", include("about.urls")),
    path("download/", include("download.urls")),
    path("feedback/", include("feedback.urls")),
    path("admin/", admin.site.urls),
    path("set-language/", set_language, name="set_language"),
    path("users/", include("users.urls")),
    path("auth/", include(django.contrib.auth.urls)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
