# documentos/models.py
from django.db import models

# Modelo para la categoría de los documentos
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

# Modelo para el documento científico
class Documento(models.Model):
    ESTADO_OPCIONES = [
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    ]
    
    nombre = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='documentos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='pendiente')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
