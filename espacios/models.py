from django.db import models
from tarifas.models import Tarifa

class Espacio(models.Model):
    ESTADO_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('OCUPADO', 'Ocupado'),
        ('RESERVADO', 'Reservado'),
        ('INACTIVO', 'Inactivo'),
    ]
    espNumero = models.CharField(max_length=25)
    espPiso = models.CharField(max_length=25)
    espTipo = models.CharField(max_length=50)
    espEstado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='DISPONIBLE')
    fkIdTarifa = models.ForeignKey(Tarifa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Numero de Espacio: {self.espNumero} - Piso: {self.espPiso} ({self.espEstado})"