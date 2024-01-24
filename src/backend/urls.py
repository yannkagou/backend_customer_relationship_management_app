from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('lead.urls')),
    path('api/v1/', include('team.urls')),
    path('api/v1/', include('client.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
