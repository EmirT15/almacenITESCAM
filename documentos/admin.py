# documentos/admin.py
from django.contrib import admin
from .models import Categoria, Documento

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'estado', 'fecha_subida')
    list_filter = ('estado', 'categoria')
    search_fields = ('nombre',)

admin.site.register(Categoria)
admin.site.register(Documento, DocumentoAdmin)
