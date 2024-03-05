import os

from django.http import FileResponse, Http404


def download_file(request, file_path):
    full_file_path = f"media/{file_path}"
    if os.path.exists(full_file_path):
        return FileResponse(open(full_file_path, "rb"), as_attachment=True)
    raise Http404("Файл не найден")
