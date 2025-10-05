from django.db import models
from clientes.models import Cliente
from servicios.models import Servicio


class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre


class Membresia(models.Model):
    id_membresia = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_cliente')
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT, db_column='id_servicio')
    fecha_inicio = models.DateField()
    fecha_vencimiento = models.DateField()
    clases_restantes = models.SmallIntegerField()

    def __str__(self):
        return f"{self.cliente} - {self.servicio}"


class EstadoPorMembresia(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, db_column='id_estado')
    membresia = models.ForeignKey(Membresia, on_delete=models.CASCADE, db_column='id_membresia')

    class Meta:
        unique_together = ('estado', 'membresia')

    def __str__(self):
        return f"{self.membresia} - {self.estado}"


class Asistencia(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    membresia = models.ForeignKey(Membresia, on_delete=models.CASCADE, db_column='id_membresia')
    fecha_asistencia = models.DateField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"Asistencia {self.fecha_asistencia} - {self.membresia}"
