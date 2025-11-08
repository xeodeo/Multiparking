from django.db import models

class Tarifa(models.Model):
    tarTipoEspacio = models.CharField(max_length=50)
    tarValorHora = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.tarTipoEspacio} - ${self.tarValorHora}/hr"