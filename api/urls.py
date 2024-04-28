from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import DocumentModelViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'docs', DocumentModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
