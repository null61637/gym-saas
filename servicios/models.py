from django.db import models


class Servicio(models.Model):
    ESTADOS = [
        ('activa', 'Activa'),
        ('inactiva', 'Inactiva')
    ]

    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    cantidad_clases = models.SmallIntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=8, choices=ESTADOS, default='activa')

    def __str__(self):
        return f"{self.nombre} (${self.precio})"
