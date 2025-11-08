from django.db import models
from usuarios.models import Usuario
from parqueos.models import Parqueo
from vehiculos.models import Vehiculo

class Novedad(models.Model):
    fkIdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fkIdParqueo = models.ForeignKey(Parqueo, null=True, blank=True, on_delete=models.SET_NULL)
    fkIdVehiculo = models.ForeignKey(Vehiculo, null=True, blank=True, on_delete=models.SET_NULL)
    novDescripcion = models.TextField()
    novFechaHora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.novFechaHora} - {self.fkIdUsuario} - {self.novDescripcion[:30]}"