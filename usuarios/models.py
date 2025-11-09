from django.db import models
from roles.models import Rol

class Usuario(models.Model):
    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    ]
    usuDocumento = models.CharField(max_length=50, unique=True)
    usuNombreCompleto = models.CharField(max_length=255)
    usuCorreo = models.EmailField(blank=True, null=True)
    usuTelefono = models.CharField(max_length=50, blank=True, null=True)
    usuClaveHash = models.CharField(max_length=255)
    usuEstado = models.CharField(max_length=8, choices=ESTADO_CHOICES, default='ACTIVO')
    usuFechaRegistro = models.DateTimeField(auto_now_add=True)
    fkIdRol = models.ForeignKey(Rol, on_delete=models.CASCADE, default= 2)
    
    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return f"{self.usuNombreCompleto} ({self.usuDocumento}) - {self.fkIdRol.rolTipoRol}"