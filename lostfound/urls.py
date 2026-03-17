# lostfound/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include all URLs from the core app
    path('', include('core.urls')),

# This line below makes uploaded images accessible in development
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)