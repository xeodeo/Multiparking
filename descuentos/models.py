from django.db import models
from pagos.models import Pago  # Asegúrate de que la app pagos esté creada y migrada

class Descuento(models.Model):
    TIPO_CHOICES = [
        ('PORCENTAJE', 'Porcentaje'),
        ('VALOR_FIJO', 'Valor fijo'),
    ]

    desNombre = models.CharField(max_length=100)
    desTipo = models.CharField(max_length=15, choices=TIPO_CHOICES)
    desValor = models.DecimalField(max_digits=10, decimal_places=2)
    desDescripcion = models.TextField(blank=True, null=True)
    desCondicion = models.CharField(max_length=255, blank=True, null=True)
    desFechaInicio = models.DateField(blank=True, null=True)
    desFechaFin = models.DateField(blank=True, null=True)
    desActivo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.desNombre} ({self.get_desTipo_display()})"

class DescuentoAplicado(models.Model):
    fkIdPago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    fkIdDescuento = models.ForeignKey(Descuento, on_delete=models.CASCADE)
    montoDescontado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pago {self.fkIdPago.id} - Descuento {self.fkIdDescuento.desNombre} (-${self.montoDescontado})"