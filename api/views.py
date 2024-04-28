from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from docs.models import Document
from docs.serializers import DocumentSerializer


class DocumentModelViewSet(ModelViewSet):
    queryset = Document.objects.all().order_by('id')
    serializer_class = DocumentSerializer

    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            self.permission_classes = [IsAuthenticated]
        return super(DocumentModelViewSet, self).get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(initiator=self.request.user)
