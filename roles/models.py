from django.db import models

class Rol(models.Model):
    rolTipoRol = models.CharField(max_length=100, unique=True)
    rolDescripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.rolTipoRol
    