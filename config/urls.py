from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.static import serve
from django.urls import re_path
from api.media_views import serve_media
import os

def home_view(request):
    """Simple home view that redirects to API docs or shows basic info"""
    return HttpResponse(
        '<h1>ALX Project Backend API</h1>'
        '<p><a href="/api/">API Endpoints</a></p>'
        '<p><a href="/admin/">Admin Panel</a></p>'
        '<p><a href="/api/health/">Health Check</a></p>'
    )

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

# Serve media files in production and development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    # Serve media files in production using custom view
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve_media, name='media'),
    ]
