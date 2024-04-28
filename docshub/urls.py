from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('docs.urls', namespace='docs')),
    path('users/', include('users.urls', namespace='users')),
    path('api/', include('api.urls', namespace='api')),
    path('api-token-auth/', views.obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
