from django.db import models


class Usuario(models.Model):
    dpi = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    password = models.CharField(max_length=60)
    correo = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    encargado = models.CharField(max_length=3)

class Cliente(models.Model):
    dpi = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    nit = models.CharField(max_length=60)
    direccion = models.CharField(max_length=150)

class Bodega(models.Model):
    id_bodega = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=60)
    estado = models.CharField(max_length=150)
    encargado = models.ForeignKey('Usuario', db_column='dpi')



# Create your models here.