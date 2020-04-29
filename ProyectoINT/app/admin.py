from django.contrib import admin
from .models import Usuario
from .models import Cliente
from .models import Bodega
from .models import Producto
from .models import Categoria
from .models import Sede
from .models import OrdenVenta
from .models import OrdenTransferencia

admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Sede)
admin.site.register(Bodega)
admin.site.register(OrdenVenta)
admin.site.register(OrdenTransferencia)