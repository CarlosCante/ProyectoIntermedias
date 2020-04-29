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
    categoria = models.ManyToManyField('Categoria')

class Categoria(models.Model):
    nombre = models.CharField(max_length=150)

    def __unicode__(self):
        return '{}'.format(self.nombre)

class Bodega(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=60)
    estado = models.CharField(max_length=150)
    encargado = models.ForeignKey('Usuario', db_column='dpi', on_delete= models.CASCADE)

class Sede(models.Model):
    alias = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    departamento = models.CharField(max_length=150)
    municipio = models.CharField(max_length=150)
    enargado = models.ForeignKey('Usuario', db_column='dpi', on_delete= models.CASCADE)

class Venta(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete= models.CASCADE)
    vendedor = models.ForeignKey('Usuario', on_delete= models.CASCADE)
    fecha_facturacion = models.DateField()
    fecha_entrega = models.DateField(null = True)

class Venta_Producto(models.Model):
    id_venta = models.ForeignKey('Venta')
    id_producto = models.ForeignKey('Producto')
    cantidad = models.IntegerField()
   


    
# Create your models here.