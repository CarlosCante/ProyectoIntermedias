from django.db import models


class USUARIO(models.Model):
    dpi = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    password = models.CharField(max_length=60)
    correo = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()

class ROL(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)

class ASIG_ROL(models.Model):
    usuario_dpi = models.ForeignKey(USUARIO, on_delete=models.CASCADE)
    rol_id = models.ForeignKey(ROL, on_delete=models.CASCADE)

class SEDE(models.Model):
    id = models.BigIntegerField(primary_key=True)
    alias = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    departamento = models.CharField(max_length=150)
    municipio = models.CharField(max_length=150)
    encargado_dpi = models.ForeignKey(USUARIO, on_delete=models.CASCADE)

class BODEGA(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)
    encargado_dpi = models.ForeignKey(USUARIO, on_delete=models.CASCADE)
    sede_id = models.ForeignKey(SEDE, on_delete=models.CASCADE)

class CLIENTE(models.Model):
    dpi = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    nit = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    sede_id = models.ForeignKey(SEDE, on_delete=models.CASCADE)

class PRODUCTO(models.Model):
    sku = models.BigIntegerField(primary_key=True)
    codigo_barras = models.CharField(max_length=150)
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)
    precio = models.BigIntegerField()

class CATEGORIA_PRODUCTO(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)

class ASIG_CATEGORIA(models.Model):
    product_sku = models.ForeignKey(PRODUCTO, on_delete=models.CASCADE)
    categoria_id = models.ForeignKey(CATEGORIA_PRODUCTO, on_delete=models.CASCADE)

class ASIG_PRODUCTO(models.Model):
    cantidad = models.BigIntegerField()
    bodega_id = models.ForeignKey(BODEGA, on_delete=models.CASCADE)
    producto_sku = models.ForeignKey(PRODUCTO, on_delete=models.CASCADE)

class ORDEN_VENTA(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fecha_facturacion = models.DateField()
    fecha_entrega = models.DateField()
    estado = models.CharField(max_length=150)
    cliente_dpi = models.ForeignKey(CLIENTE, on_delete=models.CASCADE)
    vendedor_dpi = models.ForeignKey(USUARIO, related_name='vendedor_dpi', on_delete=models.CASCADE)
    repartidor_dpi = models.ForeignKey(USUARIO, related_name='repartidor_dpi' ,on_delete=models.CASCADE)

class LISTA_PRODUCTO(models.Model):
    cantidad = models.BigIntegerField()
    orden_venta_id = models.ForeignKey(ORDEN_VENTA, on_delete=models.CASCADE)
    producto_sku = models.ForeignKey(PRODUCTO, on_delete=models.CASCADE)

class LOG_ACT_INVENTARIO(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cantidad_antigua = models.BigIntegerField()
    cantidad_nueva = models.BigIntegerField()
    motivo = models.CharField(max_length=150)
    fecha = models.DateField()
    usuario_dpi = models.ForeignKey(USUARIO, on_delete=models.CASCADE)


# Create your models here.