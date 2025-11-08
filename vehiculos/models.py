from django.db import models
from usuarios.models import Usuario

class Vehiculo(models.Model):
    vehPlaca = models.CharField(max_length=50, unique=True)
    vehTipo = models.CharField(max_length=50)
    vehColor = models.CharField(max_length=50, blank=True, null=True)
    vehMarca = models.CharField(max_length=50, blank=True, null=True)
    vehModelo = models.CharField(max_length=50, blank=True, null=True)
    fkIdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.vehPlaca