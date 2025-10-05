from django.db import models
from clientes.models import Cliente
from cajas.models import Caja
from servicios.models import Servicio


class Cobro(models.Model):
    id_cobro = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, db_column='id_cliente')
    caja = models.ForeignKey(Caja, on_delete=models.PROTECT, db_column='id_caja')
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Cobro #{self.id_cobro} - {self.cliente}"


class DetalleCobro(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT, db_column='id_servicio')
    cobro = models.ForeignKey(Cobro, on_delete=models.CASCADE, db_column='id_cobro')
    monto = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Detalle #{self.id_detalle} - {self.servicio}"


class MetodoPago(models.Model):
    id_metodo_pago = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class CobroPorMetodoPago(models.Model):
    id_cobro_metodo = models.AutoField(primary_key=True)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.PROTECT, db_column='id_metodo_pago')
    cobro = models.ForeignKey(Cobro, on_delete=models.CASCADE, db_column='id_cobro')
    monto_pago = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.metodo_pago} - ${self.monto_pago}"
