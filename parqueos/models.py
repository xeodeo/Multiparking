from django.db import models
from vehiculos.models import Vehiculo
from espacios.models import Espacio

class Parqueo(models.Model):
    parHoraEntrada = models.DateTimeField(auto_now_add=True)
    parHoraSalida = models.DateTimeField(blank=True, null=True)
    fkIdVehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fkIdEspacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)

    def __str__(self):
        entrada = self.parHoraEntrada.strftime("%Y-%m-%d %H:%M")
        salida = self.parHoraSalida.strftime("%Y-%m-%d %H:%M") if self.parHoraSalida else "En curso"
        return f"{self.fkIdVehiculo.vehPlaca} - Espacio {self.fkIdEspacio.espNumero} - {entrada} a {salida}"