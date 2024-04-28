from django.contrib.auth.decorators import login_required
from django.urls import path

from docs.views import (DocumentCreateView, DocumentDeleteView,
                        DocumentListView, DocumentUpdateView)

app_name = 'docs'

urlpatterns = [
    path('', DocumentListView.as_view(), name='index'),
    path('create/', login_required(DocumentCreateView.as_view()), name='create'),
    path('<pk>/update/', DocumentUpdateView.as_view(), name='update'),
    path('<pk>/delete/', DocumentDeleteView.as_view(), name='delete'),
]
