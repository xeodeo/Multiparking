from django.db import models
from parqueos.models import Parqueo

class Pago(models.Model):
    METODO_CHOICES = [
        ('EFECTIVO', 'Efectivo'),
        ('NEQUI', 'Nequi'),
        ('TARJETA', 'Tarjeta'),
        ('DAVIPLATA', 'Daviplata'),
    ]
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('PAGADO', 'Pagado'),
        ('CANCELADO', 'Cancelado'),
    ]
    pagFechaPago = models.DateTimeField(auto_now_add=True)
    pagMonto = models.DecimalField(max_digits=10, decimal_places=2)
    pagMetodo = models.CharField(max_length=10, choices=METODO_CHOICES, default='EFECTIVO')
    pagEstado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='PENDIENTE')
    fkIdParqueo = models.ForeignKey(Parqueo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_pagMetodo_display()} ${self.pagMonto} ({self.get_pagEstado_display()}) [{self.pagFechaPago.strftime('%Y-%m-%d %H:%M')}]"