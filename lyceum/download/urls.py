from django.urls import path
from download import views

app_name = "downloads"

urlpatterns = [
    path("<path:file_path>/", views.download_file, name="download_file"),
]
