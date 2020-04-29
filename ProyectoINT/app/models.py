from django.db import models


class Usuario(models.Model):
    dpi = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    password = models.CharField(max_length=60)
    correo = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField(null = True)
    encargado = models.CharField(max_length=3)

class Cliente(models.Model):
    dpi = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    nit = models.CharField(max_length=60)
    direccion = models.CharField(max_length=150)
    sede = models.IntegerField()

class Producto(models.Model):
    sku = models.CharField(max_length=150,primary_key=True)
    codigoBarras = models.CharField(max_length=150)
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)
    precio = models.FloatField()
    categoria = models.ManyToManyField('Categoria', db_column='id')

class Categoria(models.Model):
    nombre = models.CharField(max_length=150)

class Bodega(models.Model):
    id_bodega = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=60)
    estado = models.CharField(max_length=150)
    encargado = models.ForeignKey('Usuario', db_column='dpi')

class Sede(models.Model):
    id_sede = models.BigIntegerField(primary_key=True)
    alias = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    departamento = models.CharField(max_length=150)
    municipio = models.CharField(max_length=150)
    encargado = models.ForeignKey('Usuario', db_column='dpi')


class OrdenVenta(models.Model):
    id_venta = models.BigIntegerField(primary_key=True)
    fecha = models.DateTimeField(null=True)
    id_sede = models.ForeignKey('Sede', db_column='id_sede')
    id_bodega = models.ForeignKey('Bodega', db_column='id_bodega')
    id_producto = models.ForeignKey('Producto', db_column='sku')
    id_cliente = models.ForeignKey('Cliente', db_column='dpi')



class OrdenTransferencia(models.Model):
    id_transferencia=models.BigIntegerField(primary_key=True)
    fecha = models.DateTimeField(null=True)
    id_sede = models.ForeignKey('Sede', db_column='id_sede')
    id_bodega = models.ForeignKey('Bodega', db_column='id_bodega')
    id_producto = models.ForeignKey('Producto', db_column='sku')
    id_cliente = models.ForeignKey('Cliente', db_column='dpi')

# Create your models here.