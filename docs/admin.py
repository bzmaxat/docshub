from django.contrib import admin

from docs.models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created', 'file')
    readonly_fields = ('created',)
    search_fields = ('name',)
