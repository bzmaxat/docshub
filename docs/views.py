from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from docs.forms import DocumentForm
from docs.models import Document


class DocumentListView(TitleMixin, ListView):
    model = Document
    template_name = 'docs/documents.html'
    title = 'DocsHub'


class DocumentCreateView(TitleMixin, CreateView):
    model = Document
    form_class = DocumentForm
    template_name = 'docs/create_document.html'
    success_url = reverse_lazy('docs:index')
    success_message = 'Вы успешно добавили документ!'
    title = 'DocsHub - Добавить документ'

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(DocumentCreateView, self).form_valid(form)


class DocumentUpdateView(TitleMixin, UpdateView):
    model = Document
    form_class = DocumentForm
    template_name = 'docs/update_document.html'
    success_url = reverse_lazy('docs:index')
    title = 'DocsHub - Добавить документ'


class DocumentDeleteView(DeleteView):
    model = Document
    success_url = reverse_lazy('docs:index')
    template_name = "docs/document_confirm_delete.html"
