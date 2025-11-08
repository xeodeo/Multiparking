from django.db import models
from espacios.models import Espacio
from vehiculos.models import Vehiculo

class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('RESERVADO', 'Reservado'),
        ('CANCELADO', 'Cancelado'),
        ('FINALIZADO', 'Finalizado'),
    ]
    resFechaReserva = models.DateField()
    resHoraInicio = models.DateTimeField()
    resEstado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='RESERVADO')
    fkIdEspacio = models.ForeignKey(Espacio, on_delete=models.SET_NULL, null=True)
    fkIdVehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Reserva - Espacio {self.fkIdEspacio} - Vehículo {self.fkIdVehiculo} - {self.resEstado}"