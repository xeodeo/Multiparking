from django.db import models
from usuarios.models import Usuario

class Log(models.Model):
    logFechaHora = models.DateTimeField(auto_now_add=True)
    fkIdUsuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL)
    logAccion = models.CharField(max_length=100, blank=True, null=True)
    logTabla = models.CharField(max_length=100, blank=True, null=True)
    logIdRegistro = models.CharField(max_length=100, blank=True, null=True)
    logDescripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        usuario = self.fkIdUsuario.usuNombreCompleto if self.fkIdUsuario else "Anonimo"
        return f"{self.logFechaHora} - {usuario} - {self.logAccion}: {self.logTabla}"