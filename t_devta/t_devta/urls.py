from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('', include('devta.urls')),
path('api-auth',include('rest_framework.urls')),
path('admin/',admin.site.urls),
path('api/',include('devta.api.urls')),
]
urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
