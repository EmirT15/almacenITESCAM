# documentos/views.py
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import Documento, Categoria
from .forms import DocumentoForm

def subir_documento(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = DocumentoForm()
    
    return render(request, 'documentos/subir_documento.html', {'form': form})

def inicio(request):
    documentos = Documento.objects.filter(estado='aprobado')
    return render(request, 'documentos/inicio.html', {'documentos': documentos})

@staff_member_required
def aprobar_documentos(request):
    documentos = Documento.objects.filter(estado='pendiente')
    
    if request.method == 'POST':
        doc_id = request.POST.get('doc_id')
        nuevo_estado = request.POST.get('estado')
        documento = Documento.objects.get(id=doc_id)
        documento.estado = nuevo_estado
        documento.save()
        return redirect('aprobar_documentos')
    
    return render(request, 'documentos/aprobar_documentos.html', {'documentos': documentos})

