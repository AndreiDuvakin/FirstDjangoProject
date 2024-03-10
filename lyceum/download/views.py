from pathlib import Path

from django.conf import settings
from django.http import FileResponse, Http404


def download_file(request, file_path):
    full_file_path = Path(settings.MEDIA_ROOT) / file_path
    if full_file_path.exists():
        return FileResponse(open(full_file_path, "rb"), as_attachment=True)

    raise Http404("Файл не найден")


__all__ = []
