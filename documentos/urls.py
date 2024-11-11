# documentos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('subir/', views.subir_documento, name='subir_documento'),
    path('aprobar/', views.aprobar_documentos, name='aprobar_documentos'),
]
