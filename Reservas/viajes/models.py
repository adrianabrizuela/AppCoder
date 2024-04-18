from django.db import models

from django.utils import timezone

# Create your models here.

class Pasajeros(models.Model):
    nombre = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} - Destino: {self.destino}"


class Destino(models.Model):
    lugar_de_destino = models.CharField(max_length=100)
    fecha = models.DateField(default=timezone.now)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.lugar_de_destino} - {self.fecha}"


class Excursiones(models.Model):
    destino_excursion = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    fecha = models.DateField(default=timezone.now)
    capacidad = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.destino_excursion} - {'Disponible' if self.disponible else 'No Disponible'} - Capacidad: {self.capacidad} - Fecha: {self.fecha}"

