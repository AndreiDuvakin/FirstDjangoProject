import debug_toolbar
from django.contrib import admin
from django.urls import include, path
import lyceum.settings as settings

urlpatterns = [
    path("", include("homepage.urls")),
    path("catalog/", include("catalog.urls")),
    path("about/", include("about.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
