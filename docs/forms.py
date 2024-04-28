from django import forms
from django.forms import ModelForm

from docs.models import Document


class DocumentForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Введите название'})
    )
    description = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Введите описание'})
    )
    file = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'custom-file-input', 'type': 'file'})
    )

    class Meta:
        model = Document
        fields = ['name', 'description', 'file']
