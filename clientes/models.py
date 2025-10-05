from django.db import models


class Cliente(models.Model):
    VALIDACIONES = [
        ('si', 'Sí'),
        ('no', 'No')
    ]

    id_cliente = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=8, unique=True)
    apellido = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=50, null=True, blank=True)
    contacto = models.CharField(max_length=10, null=True, blank=True)
    contacto_emergencia = models.CharField(max_length=10, null=True, blank=True)
    validacion = models.CharField(max_length=2, choices=VALIDACIONES, default='no')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
