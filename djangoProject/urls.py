from authentication.views import RegisterView
from djangoProject import settings
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static

from rest_framework import routers

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path('api/redoc/',
         SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),
    path('api/auth/', include('rest_framework.urls')),
    path('api/', include('authentication.urls')),
    path('todos/', include('todo.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
