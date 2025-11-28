"""
Views for serving and testing media files
"""
import os
from django.conf import settings
from django.http import HttpResponse, Http404, FileResponse
from django.views.decorators.http import require_GET
from django.views.decorators.cache import cache_control
from mimetypes import guess_type


@require_GET
@cache_control(max_age=3600)  # Cache for 1 hour
def serve_media(request, path):
    """
    Serve media files with proper content types and caching.
    This view is used in production when DEBUG=False.
    """
    # Construct the full file path
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    
    # Normalize paths to prevent directory traversal attacks
    file_path = os.path.abspath(file_path)
    media_root = os.path.abspath(settings.MEDIA_ROOT)
    
    # Ensure the file is within MEDIA_ROOT
    if not file_path.startswith(media_root):
        raise Http404("File not found")
    
    # Check if file exists
    if not os.path.isfile(file_path):
        raise Http404("File not found")
    
    try:
        # Guess the content type
        content_type, _ = guess_type(file_path)
        if content_type is None:
            content_type = 'application/octet-stream'
        
        # Return the file
        response = FileResponse(
            open(file_path, 'rb'),
            content_type=content_type
        )
        
        # Add cache headers for images
        if content_type.startswith('image/'):
            response['Cache-Control'] = 'public, max-age=86400'  # 24 hours
        
        return response
        
    except (OSError, IOError):
        raise Http404("File not found")