import os
import re
from mimetypes import MimeTypes

mime = MimeTypes()

from django.conf import settings
from django.http import FileResponse, HttpResponse


def static_file(request):
    path = re.search(r'^/static/(.*)', request.path).group(1)
    paths = path.split('/')
    paths.insert(0, 'static')

    base_dir = settings.BASE_DIR
    file_path = os.path.join(base_dir, *paths)
    mime_type = mime.guess_type(file_path)

    if os.path.exists(file_path):
        return FileResponse(
            open(file_path, 'rb'),
            content_type=mime_type)
    return HttpResponse('File not found', status=404)
